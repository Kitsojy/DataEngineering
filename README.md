# 📦 Data Engineering Portfolio

Welcome to my Data Engineering Portfolio — a curated collection of hands-on projects that demonstrate my ability to build, scale, and maintain data pipelines, workflows, and analytics systems.

> This work reflects both my technical skills and my product thinking — built to support real-world data use cases like data cleaning, ETL pipelines, currency normalization, and workflow orchestration.

---

## 🔍 Projects Overview

---

### 🏦 `project-bank-etl/`  
**Multi-Currency Market Capitalization ETL Pipeline**

- Scrapes a historical Wikipedia table of global banks by market cap
- Transforms USD values into GBP, EUR, INR using exchange rates
- Saves output as both `.csv` and `.db` (SQLite)
- Includes a query stage to test the final data
- Based on IBM's Coursera Data Engineering Capstone

📁 [`project-bank-etl/`](./project-bank-etl)

---

### 🎧 `project-audible-etl/`  
**Apache Airflow-Based Audible Metadata Cleaner**

- ETL pipeline using Python and Apache Airflow
- Cleans and standardizes audiobook metadata from a raw CSV
- Handles messy text formats (e.g., `"4.5 out of 5 stars"`) and standardizes fields
- Runs as a scheduled DAG inside Airflow

📁 [`project-audible-etl/`](./project-audible-etl)

---

## 🧩 Tools & Technologies Used

| Area            | Stack / Tools                              |
|------------------|---------------------------------------------|
| Ingestion        | Python · requests · CSV files              |
| Processing       | pandas · numpy                             |
| Orchestration    | Apache Airflow                             |
| Storage          | SQLite · CSV                               |
| Visualization    | – (Optional dashboarding in future)        |
| DevOps           | Docker (for Airflow) · Git                 |

---

## 📚 Background & Learning

These projects are part of my continuous data engineering learning journey, including:

- 🎓 **IBM Data Engineering Professional Certificate** – Coursera
- ⚙️ Self-directed practice with **Apache Airflow pipelines**
- 💡 Real-world ETL and transformation challenges

---

## 📎 Documentation

Each project folder includes:

- A dedicated `README.md` explaining architecture, logic, and setup
- Code broken into modular and testable components
- Clear usage instructions for reproducibility

You'll also find:

📄 [`Capstone_Project.pdf`](./project-bank-etl/Capstone_Project.pdf) — from the IBM Coursera capstone, describing the full data pipeline (includes this ETL as one component)

---

## ✅ How to Explore

```bash
git clone https://github.com/yourusername/data-engineering-portfolio.git
cd data-engineering-portfolio

#Then navigate into a project folder:

cd project-bank-etl
# or
cd project-audible-etl
