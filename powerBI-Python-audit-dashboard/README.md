# Power BI + Python Audit Dashboard

**Overview:**  
This project combines a Python ETL script with a Power BI dashboard to visualize system access trends, audit issues by severity, and remediation statuses. It reflects a practical audit reporting workflow for internal audit teams seeking to modernize their analytics capabilities.

---

### 🔧 Files and Folders

```bash
📁 powerbi-audit-dashboard/
├── audit_etl.py             # ETL script to transform audit log CSVs
├── sample_audit_logs.csv    # Simulated raw input data
├── cleaned_audit_data.csv   # Output data used by Power BI
├── dashboard.pbix           # Interactive dashboard file
├── requirements.txt         # Dependencies for running the ETL script
└── setup.md                 # Step-by-step instructions for running the project
```

---

### 🧠 Skills Demonstrated
- **Data transformation with Python** using `pandas`
- **ETL scripting**: load, clean, and export structured CSVs for reporting
- **Audit reporting visuals**: Power BI dashboard with slicers, KPI cards, and visuals
- **Metrics displayed**: 
  - Issue severity (High/Med/Low)
  - Issue type (SOX vs. Operational)
  - Remediation status (Open/Closed)
  - Time to resolve (Aging buckets)

---

### 🔍 ETL Script Breakdown (`audit_etl.py`)
The script will:
1. Load raw audit logs from a CSV file
2. Normalize column names and formats
3. Calculate days open for unresolved issues
4. Output cleaned data to `cleaned_audit_data.csv` for Power BI

---

### 📈 Power BI Dashboard (`dashboard.pbix`)
- Uses `cleaned_audit_data.csv` as the data source
- Includes visuals like:
  - Stacked column chart: Issues by severity + status
  - Pie chart: SOX vs. Operational issues
  - Bar chart: Open issues by days open (aging buckets)
  - KPI cards: Total Issues, % Closed, Avg Days to Close
  - Filters for severity, issue type, and status

---

### 🛠️ Requirements
**requirements.txt:**
```txt
pandas
```

---

### ▶️ How to Run the ETL Script
1. Clone the repo or download the folder
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the ETL script:
   ```bash
   python audit_etl.py
   ```
5. Load `cleaned_audit_data.csv` into Power BI and connect visuals

---

### 🚀 Outcome
This project shows how modern audit teams can move beyond spreadsheets and build automated data pipelines and dashboards that:
- Improve clarity in executive reporting
- Track audit remediation in real-time
- Add value to control monitoring using data-driven visuals

---

**Stay tuned — next, we’ll build the actual ETL script together!** 👨🏽‍💻📊