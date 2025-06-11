import json
from config import JSON_PATH

def load_data():
    """Loads documents from a JSON file using a simple loop over the 'texts' key."""
    documents = []
    try:
        with open(JSON_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
            for item in data.get("texts", []):  # iterate over 'texts' list, default to empty if missing
                if isinstance(item, str): 
                    documents.append(item)
    except Exception as e:
        print(f"Error loading JSON file: {e}")
    return documents