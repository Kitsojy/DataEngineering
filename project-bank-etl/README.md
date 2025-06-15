---

## 📊 Sample Output

After transformation, the dataset includes:

- Bank name
- Market cap in USD
- Market cap in GBP, EUR, INR

| Name              | MC_USD_Billion | MC_GBP_Billion | MC_EUR_Billion | MC_INR_Billion |
|-------------------|----------------|----------------|----------------|----------------|
| JPMorgan Chase    | 380.0          | 295.4          | 345.2          | 31,390.1       |
| ICBC              | 350.5          | 272.4          | 318.4          | 28,967.3       |

*(Rates shown are illustrative)*

---

## 🧠 Key Learnings

- Hands-on experience with full ETL lifecycle
- Data cleansing and transformation logic using pandas
- Currency normalization across multiple targets
- Local database storage and querying with SQLite
- Script logging and reproducibility best practices

---

## 📎 Documentation

> 📄 `ETL_Pipeline_Workflow.pdf` — contains end-to-end pipeline architecture, steps, and logic explanation.

---

## ▶️ Running the Script

1. Clone the repo:
   ```bash
   git clone https://github.com/Kitsojy/DataEngineering.git
   cd project-bank-etl