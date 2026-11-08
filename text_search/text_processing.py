import re
from data.loader import smartphones

def normalize_text(text):
    normalized_text = re.sub(r"[^\w\s]", " ", text.lower())
    return " ".join(normalized_text.split())

def extract_budget(text):
    text = text.lower()

    currency = r"(?:евро|eur|€)"
    number = r"\d+(?:[.,]\d+)?"
    
    minimum_match = re.search(
        rf"\b(?:поне|минимум|не по-малко от)\s+({number})\s*{currency}",
        text
    )

    maximum_match = re.search(
        rf"\b(?:до|максимум|не повече от|най-много|около)\s+({number})\s*{currency}",
        text
    )
    
    range_match = re.search(
        rf"\b(?:между|от)\s+({number})\s*(?:{currency})?\s+"
        rf"(?:и|до|-)\s+(?:около\s+)?({number})\s*{currency}",
        text
    )

    dash_match = re.search(rf"\b({number})\s*[-–—]\s*({number})\s*{currency}",text)

    under_match = re.search(rf"\bпод\s+({number})\s*{currency}",text)
    
    over_match = re.search(rf"\b(?:над|повече от)\s+({number})\s*{currency}",text)
    
    single_match = re.search(rf"({number})\s*{currency}",text)

    def to_number(value):
        return int(float(value.replace(",", ".")))

    match True:
        case _ if range_match is not None:
            return to_number(range_match.group(1)), to_number(range_match.group(2))

        case _ if dash_match is not None:
            return to_number(dash_match.group(1)), to_number(dash_match.group(2))

        case _ if under_match is not None:
            return 0, to_number(under_match.group(1)) - 1

        case _ if over_match is not None:
            return to_number(over_match.group(1)) + 1, 2000

        case _ if minimum_match is not None:
            return to_number(minimum_match.group(1)), 2000

        case _ if maximum_match is not None:
            return 0, to_number(maximum_match.group(1))

        case _ if single_match is not None:
            return 0, to_number(single_match.group(1))

        case _:
            return None

def extract_phone_info(text):
    text = normalize_text(text)

    def find_name(key):
        names = sorted({phone[key] for phone in smartphones}, key=len, reverse=True)

        for name in names:
            if re.search(rf"(?<!\w){re.escape(normalize_text(name))}(?!\w)", text):
                return name

        return None

    return {"brand": find_name("brand"), "model": find_name("model")}

def extract_os(text):
    text = text.lower()

    operating_systems = {phone["os"] for phone in smartphones}

    for os in operating_systems:
        if re.search(rf"(?<!\w){re.escape(os.lower())}(?!\w)", text):
            return os

    return None

def process_text(text):
    phone_info = extract_phone_info(text)

    return {
        "text": normalize_text(text),
        "budget": extract_budget(text),
        "brand": phone_info["brand"],
        "model": phone_info["model"],
        "os": extract_os(text)
    }

