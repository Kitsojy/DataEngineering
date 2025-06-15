# 📚 Audible ETL Pipeline (Airflow)

This project is an ETL pipeline built with **Apache Airflow**, designed to clean and prepare an audiobook metadata dataset (from Audible). It processes the raw CSV file by splitting logic into extract, transform, and load tasks inside a scheduled DAG.

---

## 🔧 Stack

- Python
- Apache Airflow
- pandas
- CSV I/O

---

## 🧭 Pipeline Flow

1. **Extract:** Simulated download of raw Audible CSV  
2. **Transform:** Cleans stars, authors, narrators, prices, duration (converted to minutes)  
3. **Load:** Reads final cleaned file for verification (can be extended to load into a DB)

---

## 🗃 File Structure

project-audible-etl/
├── etl_audible_pipeline_split.py # DAG + ETL logic
├── README.md

> 🔸 Input: `audible_uncleaned.csv` expected at `/opt/airflow/data/`  
> 🔸 Output: `audible_cleaned.csv` saved at the same path after transformation

---

## 🧹 Sample Transformations

- `stars`: `"4.6 out of 5 stars"` → `4.6`
- `author`: `"Writtenby: John Doe"` → `"John Doe"`
- `narrator`: `"Narratedby: Sarah Smith"` → `"Sarah Smith"`  
- `price`: `"Free"` → `0.0`  
- `time`: `"5 hrs 30 mins"` → `330` (in `time_in_minutes`)

---

## ▶️ How to Run

> **If using Docker-based Airflow**

1. Place `audible_uncleaned.csv` in:
   `/opt/airflow/data/audible_uncleaned.csv`
2. Add this DAG to your `dags/` folder.
3. Launch Airflow:
```bash
docker-compose up -d
```
4. Trigger the DAG `etl_audible_pipeline_split` from the Airflow UI (http://localhost:8080).
   
