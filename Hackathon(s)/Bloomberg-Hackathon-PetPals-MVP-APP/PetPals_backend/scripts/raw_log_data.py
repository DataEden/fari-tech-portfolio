def parse_raw_pet_data(data):
    """
    Parses raw event data from multiple pets.

    Parameters:
    - data (list of dicts): Each item contains a pet's ID, name, and events (meals, walks, measurements).

    Returns:
    - List of summaries per pet, including:
        - Total meals
        - Total walks
        - Last known weight (if available)
    """
    results = []

    for pet in data:
        pet_id = pet.get("pet_id")
        name = pet.get("pet_name", "Unknown")
        events = pet.get("events", [])

        # Count event types
        walk_count = sum(1 for e in events if e["type"] == "walk")
        meal_count = sum(1 for e in events if e["type"] == "meal")

        # Get latest weight measurement
        weights = [
            (e["timestamp"], e["value"]) for e in events
            if e["type"] == "measurement" and "lbs" in e["value"]
        ]
        last_weight = max(weights, key=lambda x: x[0])[1] if weights else "N/A"

        results.append({
            "pet_id": pet_id,
            "pet_name": name,
            "total_meals": meal_count,
            "total_walks": walk_count,
            "last_known_weight": last_weight
        })

    return results

"""
example usage: 
summary = parse_raw_pet_data(your_api_response_data)
print(json.dumps(summary, indent=2))

"""