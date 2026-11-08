from text_search.text_processing import process_text
from expert_system.recommender import filter_phones

def retrieve_phones(text):
    requirements = process_text(text)

    candidates = filter_phones({
        "budget": requirements["budget"] or (0, float("inf")),
        "os": requirements["os"]
    })

    for key in ("brand", "model"):
        if requirements[key]:
            candidates = [
                phone for phone in candidates
                if phone[key] == requirements[key]
            ]

    return candidates
