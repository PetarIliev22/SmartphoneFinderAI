import json
from pathlib import Path

def load_json(filename):
    path = Path(__file__).parent / filename

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

smartphones = load_json("dataset.json")
explanations = load_json("explanations.json")
search_terms = load_json("search_terms.json")

PURPOSE_TERMS = search_terms["PURPOSE_TERMS"]
FEATURE_TERMS = search_terms["FEATURE_TERMS"]

PURPOSE_LABELS = explanations["PURPOSE_LABELS"]
FEATURE_LABELS = explanations["FEATURE_LABELS"]