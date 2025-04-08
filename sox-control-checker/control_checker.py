import pandas as pd # Importing pandas for data manipulation
import os # Importing os for file handling

folder = "sample_logs"
violations = [] # List to store violations

# Check if the folder exists
for file in os.listdir(folder):
    # Check if the file is a CSV file
    if file.endswith(".csv"):
        # Read each CSV file in the folder
        df = pd.read_csv(os.path.join(folder, file))
        # Check if the required columns exist
        bad_users = df[(df['status'] == 'terminated') & (df['access_granted'] == True)]
        if not bad_users.empty: # If there are any violations
            # Print the violations
            print(f"\n[!] Violations in {file}:")
            # Print the bad users
            print(bad_users) 
              # Append the violations to the list
            violations.append(bad_users)
# Save the violations to a CSV file
if violations:
    result = pd.concat(violations) # Concatenate all violations into a single DataFrame
    result.to_csv("violations_report.csv", index=False) # Save the DataFrame to a CSV file
    print("\nAll violations saved to violations_report.csv") # Print the path of the saved file
else:
    print("\n✅ No control violations found.")