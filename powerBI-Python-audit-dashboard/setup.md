
# Setup Instructions

This guide will help you get started with the Power BI + Python Audit Dashboard project.

---

## 1. Clone the Repository

```bash
git clone https://github.com/DataEden/fari-tech-portfolio.git
cd fari-tech-portfolio/powerbi-audit-dashboard
```

---

## 2. Set Up the Python Environment (Optional)

If you're using Python, create a virtual environment:

### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Required Packages

```bash
pip install -r requirements.txt
```

---

## 4. Run the ETL Script

Make sure you have `sample_audit_logs.csv` in the folder, then run:

```bash
python audit_etl.py
```

---

## 5. Load Data into Power BI

- Open `dashboard.pbix`
- Load the generated `cleaned_audit_data.csv` file
- Refresh visuals and interact with filters and slicers

---

## 💡 Tips
- If you're new to Power BI, check out [Microsoft’s Beginner Guide](https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-overview)
- You can modify the ETL script to work with your real audit data logs
