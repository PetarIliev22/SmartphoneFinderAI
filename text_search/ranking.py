from functools import lru_cache
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data.loader import (
    RULE_TERMS, RULE_GROUPS, PURPOSE_LABELS, FEATURE_LABELS
)
from data.rules import rules
from expert_system.recommender import check_rule
from text_search.retrieval import retrieve_phones
from text_search.indexer import build_index
from text_search.text_processing import normalize_text
from text_search.document_builder import build_document

@lru_cache(maxsize=1)
def build_rules_index():
    names, phrases = [], []

    for name, terms in RULE_TERMS.items():
        for phrase in terms if isinstance(terms, list) else [terms]:
            names.append(name)
            phrases.append(phrase)

    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    matrix = vectorizer.fit_transform(phrases)

    return names, vectorizer, matrix

def detect_rules(text):
    names, vectorizer, matrix = build_rules_index()
    words = normalize_text(text).split()

    if not words:
        return []

    normalized_text = f" {' '.join(words)} "

    phrases = [
        " ".join(words[i:i + size])
        for size in (1, 2, 3)
        for i in range(len(words) - size + 1)
    ]

    similarities = cosine_similarity(vectorizer.transform(phrases), matrix)
    detected = []

    for members in RULE_GROUPS.values():
        best_name, best_score = None, 0.35

        for name in members:
            if name not in RULE_TERMS:
                continue

            terms = RULE_TERMS[name]

            if isinstance(terms, list):
                score = max(
                    (
                        1 + len(term.split()) / 100
                        for term in terms
                        if f" {normalize_text(term)} " in normalized_text
                    ),
                    default=0
                )
            else:
                score = max(
                    (
                        similarities[:, i].max()
                        for i, rule_name in enumerate(names)
                        if rule_name == name
                    ),
                    default=0
                )

                if any(
                    len(phrase.split()) >= 2
                    and f" {phrase} " in f" {terms} "
                    for phrase in phrases
                ):
                    score = 1.0

            if score > best_score:
                best_name, best_score = name, score

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

    similarities = cosine_similarity(
        vectorizer.transform([text]),
        vectorizer.transform(
            [build_document(phone) for phone in candidates]
        )
    )[0]

    detected = detect_rules(text)
    scored = []

    for phone, similarity in zip(candidates, similarities):
        score = (
            0.7 * technical_score(phone, detected)
            + 0.3 * similarity
        )
        scored.append((phone, score))

    scored.sort(key=lambda item: item[1], reverse=True)
    return [phone for phone, _ in scored]

def explain_phone(phone, text):
    purposes, features = [], []

    for name in detect_rules(text):
        rule = rules.get(name, {}).get(True)

        if not rule or not check_rule(phone, rule):
            continue

        if name in PURPOSE_LABELS:
            purposes.append(PURPOSE_LABELS[name])

        field = rule[0]

        if field in FEATURE_LABELS:
            label = FEATURE_LABELS[field]

            if label not in features:
                features.append(label)

    explanation = "Този смартфон е подходящ за твоите нужди."

    if purposes:
        explanation = (
            "Този смартфон е подходящ за "
            + ", ".join(purposes) + "."
        )

    if features:
        explanation += (
            "\n\nОсновните му предимства са: "
            + ", ".join(features) + "."
        )

    return explanation

def recommend_phone(text):
    if len(text.strip()) < 5:
        return None

    ranked = rank_phones(text)
    return ranked[0] if ranked else None


if __name__ == "__main__":
    tests = [
        "Търся смартфон за работа, с който да използвам много приложения едновременно и да съхранявам документи.",

        "Искам телефон за фотография, който да прави качествени снимки, да има оптична стабилизация и оптичен zoom.",

        "Търся геймърски смартфон за тежки игри, с много RAM, голям екран и издръжлива батерия.",

        "Искам компактен телефон с малък дисплей, който да използвам за ежедневни задачи и разговори.",

        "Търся смартфон за гледане на филми и сериали, с голям дисплей и висока честота на опресняване.",

        "Искам телефон за заснемане на видео, който поддържа 4K при 60 fps и има оптична стабилизация.",

        "Търся телефон с голяма батерия, бързо зареждане и възможност за безжично зареждане.",

        "Искам смартфон с много пространство за съхранение, защото пазя голям брой файлове и документи.",

        "Търся компактен смартфон с малка батерия, бавно зареждане и стандартна честота на опресняване.",

        "Искам телефон за пътувания и използване навън, с дълга автономност и голям капацитет на батерията.",

        "Търся смартфон за професионално видеозаснемане с 8K резолюция, ProRes и ултраширока камера.",

        "Искам телефон за ежедневна употреба до 600 евро, с добра камера, бързо зареждане и достатъчно място за файлове."
    ]

    for i, text in enumerate(tests, 1):
        print(f"\n{'=' * 60}")
        print(f"ТЕСТ {i}")
        print(f"Заявка: {text}")
        print(f"Правила: {detect_rules(text)}")
