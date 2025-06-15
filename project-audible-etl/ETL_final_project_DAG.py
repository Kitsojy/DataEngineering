from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import os

# Global file path
RAW_FILE_PATH = "/opt/airflow/data/audible_uncleaned.csv"
CLEAN_FILE_PATH = "/opt/airflow/data/audible_cleaned.csv"

def extract():
    print("Extracting data...")
    #kagglehub.dataset_download("snehangsude/audible-dataset")
    print(f"Data extracted to: {RAW_FILE_PATH}")

def transform():
    print("Transforming data...")

    if not os.path.exists(RAW_FILE_PATH):
        raise FileNotFoundError(f"{RAW_FILE_PATH} does not exist. Make sure 'extract' ran successfully.")

    df = pd.read_csv(RAW_FILE_PATH)
    df_copy = df.copy()

    df_copy['stars'] = (
        df_copy['stars']
        .str.replace(r'out.*', '', regex=True)
        .str.replace('Not rated yet', '0')
        .astype(float)
    )

    df_copy['author'] = (
        df_copy['author']
        .astype(str)
        .str.replace('Writtenby:', '', regex=False)
        .apply(lambda x: x.split(',')[0])
    )

    df_copy['narrator'] = (
        df_copy['narrator']
        .astype(str)
        .str.replace('Narratedby:', '', regex=False)
        .apply(lambda x: x.split(',')[0])
    )
    df_copy.loc[df_copy['narrator'].isin(['anonymous', 'Intuitive', 'uncredited']), 'narrator'] = 'Unknown'

    df_copy['price'] = (
        df_copy['price']
        .astype(str)
        .str.replace('Free', '0')
        .str.replace(',', '')
        .astype(float)
    )

    df_copy['time'] = df_copy['time'].astype(str)
    df_copy['hours'] = df_copy['time'].str.extract(r'(\d+)\s*hrs?').astype(float).fillna(0)
    df_copy['minutes'] = df_copy['time'].str.extract(r'(\d+)\s*mins?').astype(float).fillna(0)
    df_copy['time_in_minutes'] = (df_copy['hours'] * 60 + df_copy['minutes']).astype(int)

    df_copy.drop(columns=['hours', 'minutes', 'time'], inplace=True)

    df_copy['name'] = df_copy['name'].astype(str)
    df_copy['releasedate'] = pd.to_datetime(df_copy['releasedate'])
    df_copy['language'] = df_copy['language'].astype(str)

    # Save intermediate result to CSV for the load step
    df_copy.to_csv(CLEAN_FILE_PATH, index=False)
    print("Data transformed and saved to intermediate file.")

def load():
    print("Loading data...")

    if not os.path.exists(CLEAN_FILE_PATH):
        raise FileNotFoundError(f"{CLEAN_FILE_PATH} does not exist. Make sure 'transform' ran successfully.")

    df = pd.read_csv(CLEAN_FILE_PATH)
    print(f"Loaded cleaned data with {len(df)} records.")
    print("You can now load it to a database or another system if needed.")

# ------------------ Airflow DAG ------------------

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='etl_audible_pipeline_split',
    default_args=default_args,
    description='ETL pipeline split into extract, transform, and load tasks',
    schedule='@daily',
    start_date=datetime(2025, 5, 20),
    catchup=False,
    tags=['etl', 'audible'],
) as dag:

    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load
    )

    # Set task dependencies: extract >> transform >> load
    extract_task >> transform_task >> load_task
