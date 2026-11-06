import json
from pathlib import Path

def load_json(filename):
    path = Path(__file__).parent / filename

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

smartphones = load_json("dataset.json")
