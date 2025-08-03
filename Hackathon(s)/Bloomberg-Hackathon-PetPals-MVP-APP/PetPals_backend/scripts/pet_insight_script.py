import pandas as pd

def analyze_csv_logs(health_path="mock_health_logs.csv", task_path="mock_task_logs.csv"):
    """
    Analyze mood and task completion trends from CSV logs.

    Parameters:
    - health_path: Path to the health logs CSV
    - task_path: Path to the task logs CSV

    Returns:
    - dict: A dictionary containing summary metrics and alert flags
    """

    # Load mock data
    health_logs = pd.read_csv(health_path)
    task_logs = pd.read_csv(task_path)

    print("=== Mood Trend Summary ===")
    low_moods = health_logs[health_logs['mood'] == 'low']
    print(f"Total days with 'low' mood: {len(low_moods)}")

    health_logs['low_flag'] = health_logs['mood'] == 'low'
    health_logs['low_streak'] = health_logs['low_flag'].astype(int).rolling(2).sum()
    if (health_logs['low_streak'] >= 2).any():
        print("🐶 Detected a 2+ day low mood streak.")

    print("\n=== Missed Task Summary ===")
    task_logs['missed_feedings'] = (task_logs['feeding_8am'] + task_logs['feeding_6pm']) < 2
    task_logs['missed_walks'] = (task_logs['walk_morning'] + task_logs['walk_evening']) < 2

    missed_feeding_days = task_logs['missed_feedings'].sum()
    missed_walk_days = task_logs['missed_walks'].sum()

    print(f"Days with missed feedings: {missed_feeding_days}")
    print(f"Days with missed walks: {missed_walk_days}")

    if missed_feeding_days >= 3:
        print("🍚 3 or more days of missed feedings.")
    if missed_walk_days >= 3:
        print("🐕 3 or more days of missed walks.")

    return {
        "total_low_mood_days": len(low_moods),
        "missed_feeding_days": int(missed_feeding_days),
        "missed_walk_days": int(missed_walk_days),
        "consecutive_low_mood_streak": (health_logs['low_streak'] >= 2).any()
    }
