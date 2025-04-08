## **Project 1: SOX Control Testing Automation with Python**

**Overview:**  
This project simulates a typical SOX (Sarbanes-Oxley) IT General Controls (ITGC) testing task using Python. It demonstrates the use of Python to read, parse, and validate control evidence data across multiple CSV logs.

**Skills Demonstrated:**  
- Python (pandas, os)  
- Control evaluation logic  
- Automation scripting for control evidence checks  
- Clean, commented code and audit-read documentation  

**Folder Structure:**  
```
📁 sox-control-checker/
├── control_checker.py
├── sample_logs/
│   ├── system1.csv
│   └── system2.csv
├── README.md
└── requirements.txt
```

**How It Works:**  
- Parses all CSV logs in the `sample_logs/` directory  
- Flags users marked as `terminated` who still have `access_granted = True`  
- Outputs a summary in the console and a CSV report of all violations  

**How to Run:**  
1. Clone the repo or copy files locally  
2. Install dependencies using the `requirements.txt` file  
3. Run the script `control_checker.py`  
4. Review the generated `violations_report.csv` for flagged entries  

**Why This Matters:**  
This kind of automation saves time during quarterly SOX testing cycles, improves accuracy, and demonstrates how auditors can apply scripting skills to streamline review tasks.
