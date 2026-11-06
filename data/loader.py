import json
from pathlib import Path

def load_json(filename):
    path = Path(__file__).parent / filename

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

smartphones = load_json("dataset.json")
explanations = load_json("explanations.json")

PURPOSE_LABELS = explanations["PURPOSE_LABELS"]
FEATURE_LABELS = explanations["FEATURE_LABELS"]