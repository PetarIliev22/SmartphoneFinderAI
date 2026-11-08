import re

from functools import lru_cache
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data.loader import RULE_TERMS, RULE_GROUPS
from data.rules import rules
from expert_system.recommender import check_rule
from text_search.retrieval import retrieve_phones
from text_search.indexer import build_index
from text_search.document_builder import build_document

@lru_cache(maxsize=1)
def build_rules_index():
    names = []
    phrases = []

    for name, terms in RULE_TERMS.items():
        for phrase in terms if isinstance(terms, list) else [terms]:
            names.append(name)
            phrases.append(phrase)

    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    matrix = vectorizer.fit_transform(phrases)

    return names, vectorizer, matrix

def detect_rules(text):
    names, vectorizer, matrix = build_rules_index()
    words = re.findall(r"\w+", text.lower())

    if not words:
        return []

    normalized_text = f" {' '.join(words)} "

    phrases = [
        " ".join(words[i:i + size])
        for size in (1, 2, 3)
        for i in range(len(words) - size + 1)
    ]

    similarities = cosine_similarity(
        vectorizer.transform(phrases), matrix
    )

    detected = []

    for members in RULE_GROUPS.values():
        best_name = None
        best_score = 0.35

        for name in members:
            if name not in RULE_TERMS:
                continue

            terms = RULE_TERMS[name]

            if isinstance(terms, list):
                matches = [
                    phrase for phrase in terms
                    if f" {' '.join(re.findall(r'\w+', phrase.lower()))} "
                    in normalized_text
                ]

                score = max(
                    (1 + len(phrase.split()) / 100 for phrase in matches),
                    default=0
                )
            else:
                score = max(
                    (similarities[:, i].max()
                     for i, rule_name in enumerate(names)
                     if rule_name == name),
                    default=0
                )

            if score > best_score:
                best_name = name
                best_score = score

        if best_name:
            detected.append(best_name)

    return detected

def technical_score(phone, detected_rules):
    if not detected_rules:
        return 0

    matched = sum(
        check_rule(phone, rules[name][True])
        for name in detected_rules
    )

    return matched / len(detected_rules)

def rank_phones(text):
    candidates = retrieve_phones(text)

    if not candidates:
        return []

    vectorizer, _ = build_index()
    documents = [build_document(phone) for phone in candidates]

    similarities = cosine_similarity(
        vectorizer.transform([text]),
        vectorizer.transform(documents)
    )[0]

    detected = detect_rules(text)
    scored = []

    for phone, similarity in zip(candidates, similarities):
        technical = technical_score(phone, detected)
        score = 0.7 * technical + 0.3 * similarity
        scored.append((phone, score))

    scored.sort(key=lambda item: item[1], reverse=True)

    return [phone for phone, score in scored]

def recommend_phone(text):
    ranked = rank_phones(text)
    return ranked[0] if ranked else None

