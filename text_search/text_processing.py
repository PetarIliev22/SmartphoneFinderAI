import re

from functools import lru_cache
from data.loader import smartphones

def normalize_text(text):
    return " ".join(re.sub(r"[^\w\s]", " ", text.lower()).split())

def extract_budget(text):
    text = text.lower()

    currency = r"(?:евро|eur|€)"
    number = r"\d+(?:[.,]\d+)?"

    patterns = [
        (
            rf"\b(?:между|от)\s+({number})\s*(?:{currency})?\s+"
            rf"(?:и|до|-)\s+(?:около\s+)?({number})\s*{currency}",
            "range"
        ),
        (rf"\b({number})\s*[-–—]\s*({number})\s*{currency}", "range"),
        (rf"\bпод\s+({number})\s*{currency}", "under"),
        (rf"\b(?:над|повече от)\s+({number})\s*{currency}", "over"),
        (
            rf"\b(?:поне|минимум|не по-малко от)\s+({number})\s*{currency}",
            "minimum"
        ),
        (
            rf"\b(?:до|максимум|не повече от|най-много|около)\s+({number})\s*{currency}",
            "maximum"
        ),
        (rf"({number})\s*{currency}", "maximum")
    ]

    for pattern, kind in patterns:
        match = re.search(pattern, text)

        if not match:
            continue

        values = [
            int(float(value.replace(",", ".")))
            for value in match.groups()
        ]

        match kind:
            case "range":
                return values[0], values[1]
            case "under":
                return 0, values[0] - 1
            case "over":
                return values[0] + 1, 2000
            case "minimum":
                return values[0], 2000
            case "maximum":
                return 0, values[0]

    return None

@lru_cache(maxsize=None)
def get_phone_names(key):
    return sorted(
        {phone[key] for phone in smartphones},
        key=len,
        reverse=True
    )

def extract_phone_info(text):
    text = normalize_text(text)

    def find_name(key):
        for name in get_phone_names(key):
            if re.search(
                rf"(?<!\w){re.escape(normalize_text(name))}(?!\w)",
                text
            ):
                return name

        return None

    return {
        "brand": find_name("brand"),
        "model": find_name("model")
    }

def extract_os(text):
    text = text.lower()

    for os in get_phone_names("os"):
        if re.search(rf"(?<!\w){re.escape(os.lower())}(?!\w)", text):
            return os

    return None

def process_text(text):
    return {
        "text": normalize_text(text),
        "budget": extract_budget(text),
        **extract_phone_info(text),
        "os": extract_os(text)
    }
