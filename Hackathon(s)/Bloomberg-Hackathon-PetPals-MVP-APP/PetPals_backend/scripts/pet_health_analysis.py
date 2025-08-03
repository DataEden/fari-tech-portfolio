from collections import Counter
from datetime import datetime

def analyze_pet_health_and_activity(data):
    """
    Analyze a pet's health and task activity based on JSON-formatted input.

    Parameters:
    - data (dict): A dictionary containing structured JSON with fields:
        {
          "pet_name": "Baki",
          "logs": {
              "health": [ {...}, ... ],
              "tasks": [ {...}, ... ]
          }
        }

    Returns:
    - dict: A structured insight report including:
        - pet_name
        - total_low_mood_days
        - missed_feeding_days
        - missed_walk_days
        - mood_counts (Counter of all moods)
        - alerts (List of important flags)
        - report_generated_on (timestamp of report)
    """

    # Extract relevant sections
    pet_name = data.get("pet_name", "Unknown Pet")
    health_logs = data.get("logs", {}).get("health", [])
    task_logs = data.get("logs", {}).get("tasks", [])

    # -------------------------------
    # Health Log Analysis
    # -------------------------------
    mood_counts = Counter(entry["mood"] for entry in health_logs)
    low_mood_days = [
        entry["date"] for entry in health_logs
        if entry["mood"] == "low"
    ]

    # -------------------------------
    # Task Log Analysis
    # -------------------------------
    missed_feedings = [
        entry["date"] for entry in task_logs
        if (entry.get("feeding_8am", 0) + entry.get("feeding_6pm", 0)) < 2
    ]
    missed_walks = [
        entry["date"] for entry in task_logs
        if (entry.get("walk_morning", 0) + entry.get("walk_evening", 0)) < 2
    ]

    # -------------------------------
    # Insight/Alert Logic
    # -------------------------------
    alerts = []
    if len(low_mood_days) >= 2:
        alerts.append("⚠️ Multiple low mood days detected.")
    if len(missed_feedings) >= 3:
        alerts.append("⚠️ 3 or more missed feeding days.")
    if len(missed_walks) >= 3:
        alerts.append("⚠️ 3 or more missed walking days.")

    # -------------------------------
    # Build Summary Output
    # -------------------------------
    summary = {
        "pet_name": pet_name,
        "total_low_mood_days": len(low_mood_days),
        "missed_feeding_days": len(missed_feedings),
        "missed_walk_days": len(missed_walks),
        "mood_counts": dict(mood_counts),
        "alerts": alerts,
        "report_generated_on": datetime.now().strftime("%Y-%m-%d")
    }

    return summary

"""
Example usage:
report = analyze_pet_health_and_activity(json_data)
print(json.dumps(report, indent=2))

"""
