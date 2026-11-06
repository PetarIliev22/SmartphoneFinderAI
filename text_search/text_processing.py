import re

def normalize_text(text):
    normalized_text = re.sub(r"[^\w\s]", " ", text.lower())
    normalized_text = re.sub(r"\s+", " ", normalized_text).strip()
    return normalized_text