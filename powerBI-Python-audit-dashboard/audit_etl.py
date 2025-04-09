
import pandas as pd
import os

# Filepaths
INPUT_FILE = "data/raw/audit_logs.csv"
OUTPUT_FILE = "data/processed/audit_summary.csv"

# Create output directory if it doesn't exist
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

# Load audit logs
df = pd.read_csv(INPUT_FILE)

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Clean data
df["issue_status"] = df["issue_status"].str.strip().str.lower()
df["issue_severity"] = df["issue_severity"].str.strip().str.lower()
df["issue_type"] = df["issue_type"].str.strip().str.lower()

# Summary metrics
summary = df.groupby(["issue_severity", "issue_status"]).size().unstack(fill_value=0)

# Output to CSV
summary.to_csv(OUTPUT_FILE)
print(f"Audit summary saved to: {OUTPUT_FILE}")
