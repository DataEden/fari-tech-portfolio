**Project 1: SOX Control Testing Automation with Python**

**Overview:**
This project simulates a typical SOX (Sarbanes-Oxley) IT General Controls (ITGC) testing task using Python. It demonstrates the use of Python to read, parse, and validate control evidence data across multiple CSV logs.

**Skills Demonstrated:**
- Python (pandas, os)
- Control evaluation logic
- Automation scripting for control evidence checks
- Clean, commented code and audit-read documentation

**Folder Structure:**
```bash
📁 sox-control-checker/
├── control_checker.py
├── sample_logs/
│   ├── system1.csv
│   └── system2.csv
├── README.md
└── requirements.txt
```

**control_checker.py (full script):**
```python
import pandas as pd
import os

folder = "sample_logs"
violations = []

for file in os.listdir(folder):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(folder, file))
        bad_users = df[(df['status'] == 'terminated') & (df['access_granted'] == True)]
        if not bad_users.empty:
            print(f"\n[!] Violations in {file}:")
            print(bad_users)
            violations.append(bad_users)

if violations:
    result = pd.concat(violations)
    result.to_csv("violations_report.csv", index=False)
    print("\nAll violations saved to violations_report.csv")
else:
    print("\n✅ No control violations found.")
```

**Sample Data – `sample_logs/system1.csv`:**
```csv
user_id,email,status,access_granted,last_login
001,jane.doe@company.com,terminated,True,2023-10-12
002,john.smith@company.com,active,True,2024-01-18
```

**Sample Data – `sample_logs/system2.csv`:**
```csv
user_id,email,status,access_granted,last_login
003,sarah.connor@company.com,terminated,True,2024-02-10
004,lee.chen@company.com,terminated,False,2023-11-02
```

**README.md (content):**
```
# SOX Control Checker

This Python tool automates the review of system access logs to identify SOX ITGC violations such as terminated users with active accounts.

## How It Works
- Parses all CSV logs in the `sample_logs/` directory
- Flags users marked as `terminated` who still have `access_granted = True`
- Outputs a summary in the console and a CSV report of all violations

## How to Run
1. Clone the repo or copy files locally
2. Install dependencies:
   ```bash
   pip install pandas
   ```
3. Run the script:
   ```bash
   python control_checker.py
   ```
4. Check `violations_report.csv` for flagged entries

## Why This Matters
This kind of automation saves time during quarterly SOX testing cycles, improves accuracy, and demonstrates how auditors can apply scripting skills to streamline review tasks.
```

**requirements.txt:**
```
pandas
```

**Outcome:**
This project gives you a foundational, resume-ready internal audit automation tool to showcase during interviews. It can also be extended further with real access logs, additional rules, or output formatting for audit reports.

---

**Project 2: Power BI + Python Audit Dashboard**

**Overview:**
This project combines a Python ETL script with a Power BI dashboard that visualizes system access trends, audit issues by severity, and remediation statuses.

**Skills Demonstrated:**
- Data transformation using Python (pandas)
- Dashboard design in Power BI
- Visual storytelling and metric reporting (KRI/KPI)
- Audit-focused visuals: open vs. closed issues, SOX vs. operational issues, aging buckets

**Files:**
- `audit_etl.py`: Reads and cleans audit logs or issue tracker CSVs, outputs summarized data for Power BI.
- `dashboard.pbix`: Power BI file showing interactive audit visuals
- `README.md`: Describes how the data flows from raw logs to visual insights

**Outcome:**
Demonstrates how modern auditors can use visualization and automation to track progress, prioritize risks, and report findings to executives with clarity.

---
Let me know when you want to dive into building the Power BI pipeline next!

