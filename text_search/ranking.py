from sklearn.metrics.pairwise import cosine_similarity
from data.loader import smartphones, PURPOSE_TERMS, FEATURE_TERMS
from text_search.indexer import build_index
from text_search.retrieval import retrieve_phones

def detect_preferences(text, vectorizer):
    terms = {**PURPOSE_TERMS, **FEATURE_TERMS}

    query_vector = vectorizer.transform([text])
    term_vectors = vectorizer.transform(list(terms.values()))

    scores = cosine_similarity(query_vector, term_vectors)[0]

    return dict(zip(terms.keys(), scores))

def technical_score(phone, candidates, preferences):
    scores = []

    for feature, weight in preferences.items():
        value = phone.get(feature)

        if not isinstance(value, (int, float)) or isinstance(value, bool):
            continue

        maximum = max(
            (p.get(feature) or 0)
            for p in candidates
        )

        if maximum > 0:
            scores.append(weight * value / maximum)

    return sum(scores) / sum(preferences.values()) if scores and sum(preferences.values()) else 0

def rank_phones(text):
    candidates = retrieve_phones(text)

    if not candidates:
        return []

    vectorizer, matrix = build_index()
    query_vector = vectorizer.transform([text])

    similarities = cosine_similarity(query_vector, matrix)[0]
    preferences = detect_preferences(text, vectorizer)

    def score(phone):
        similarity = similarities[smartphones.index(phone)]
        technical = technical_score(phone, candidates, preferences)

        return 0.6 * similarity + 0.4 * technical

    return sorted(candidates, key=score, reverse=True)

if __name__ == "__main__":
    phones = rank_phones(
        "Искам телефон за игри с повече RAM и плавен дисплей"
    )

    for phone in phones[:5]:
        print(
            phone["brand"],
            phone["model"],
            "RAM:", phone["ram"],
            "Hz:", phone["refresh_rate"]
        )

