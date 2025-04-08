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