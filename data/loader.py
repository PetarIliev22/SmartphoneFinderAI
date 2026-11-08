import json
from pathlib import Path

def load_json(filename):
    with open(Path(__file__).parent / filename, encoding="utf-8") as file:
        return json.load(file)

smartphones = load_json("dataset.json")

PURPOSE_LABELS, FEATURE_LABELS = load_json("explanations.json").values()
PURPOSE_TERMS, FEATURE_TERMS = load_json("search_terms.json").values()