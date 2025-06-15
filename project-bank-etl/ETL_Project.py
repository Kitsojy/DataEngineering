from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime 

def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' 
    now = datetime.now()  
    timestamp = now.strftime(timestamp_format) 
    with open("./project-bank-etl/code_log.txt","a") as f: 
        f.write(timestamp + ' : ' + message + '\n')    


def extract(url, table_attribs):
    page = requests.get(url).text
    data = BeautifulSoup(page,'html.parser')
    df = pd.DataFrame(columns=table_attribs)
    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr')
    for row in rows:
        col = row.find_all('td')
        if len(col)!=0 :
            MC_USD_Billion = col[2].text.strip()
            MC_USD_Billion = float(MC_USD_Billion.replace(',', ''))

            data_dict = {"Name" : col[1].text.strip(),
                        "MC_USD_Billion" : MC_USD_Billion }
                
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df,df1], ignore_index=True)
    return df



def transform(df, csv_path):
    dict_frame = pd.read_csv(csv_path)
    dict_frame = dict_frame.set_index('Currency').to_dict()['Rate']

    df['MC_GBP_Billion'] = [np.round(x*dict_frame['GBP'],2) 
    for x in df['MC_USD_Billion']]

    df['MC_EUR_Billion'] = [np.round(x*dict_frame['EUR'],2) 
    for x in df['MC_USD_Billion']]

    df['MC_INR_Billion'] = [np.round(x*dict_frame['INR'],2) 
    for x in df['MC_USD_Billion']]

    return df

def load_to_csv(df, output_path):
    df.to_csv(output_path)

def load_to_db(df, sql_connection, table_name):
   df.to_sql(table_name, sql_connection, if_exists='replace',
    index=False)

def run_query(query_statement, sql_connection):
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)


url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'

table_attribs = ['Name', 'MC_USD_Billion']
csv_path = './project-bank-etl/Largest_banks_data.csv'
exchange_rate = './project-bank-etl/exchange_rate.csv'
db_name = './project-bank-etl/Banks.db'
table_name = 'Largest_banks'

log_progress('Preliminaries complete. Initiating ETL process')

df = extract(url,table_attribs)
log_progress('Data extraction complete. Initiating Transformation process')

df = transform(df, exchange_rate)
log_progress('Data transformation complete. Initiating loading process')

load_to_csv(df, csv_path)
log_progress('Data saved to CSV file')

sql_connection = sqlite3.connect(db_name)
log_progress('SQL Connection initiated.')

load_to_db(df, sql_connection, table_name)
log_progress('Data loaded to Database as table. Running the query')

query_statement = f"SELECT Name from Largest_banks LIMIT 5"
run_query(query_statement, sql_connection)

log_progress('Process Complete.')
sql_connection.close()
