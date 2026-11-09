
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent

def load_json(filename):
    with open(DATA_DIR / filename, encoding="utf-8") as file:
        return json.load(file)

smartphones = load_json("dataset.json")

explanations = load_json("explanations.json")
PURPOSE_LABELS = explanations["PURPOSE_LABELS"]
FEATURE_LABELS = explanations["FEATURE_LABELS"]

search_terms = load_json("search_terms.json")
PURPOSE_TERMS = search_terms["PURPOSE_TERMS"]
FEATURE_TERMS = search_terms["FEATURE_TERMS"]
RULE_TERMS = search_terms["RULE_TERMS"]
RULE_GROUPS = search_terms["RULE_GROUPS"]
