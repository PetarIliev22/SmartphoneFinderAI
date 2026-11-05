
import operator

from data.dataset import smartphones
from data.questions import questions
from data.rules import rules


OPERATORS = {
    ">=": operator.ge,
    "<=": operator.le,
    ">": operator.gt,
    "<": operator.lt,
    "==": operator.eq,
    "contains": lambda a, b: b in a
}

PRIORITIES = {
    "work": ["ram", "storage", "battery", "charging_w"],
    "gaming": ["refresh_rate", "ram", "battery", "storage"],
    "photos": ["ois", "telephoto_optical_zoom", "ultrawide_mp", "storage"],
    "video": ["video_4k_fps", "ois", "storage", "battery"],
    "daily": ["battery", "charging_w", "storage", "refresh_rate"]
}


def get_next_question(question_id, answer):
    next_question = questions[question_id]["next"]

    if isinstance(next_question, dict):
        return next_question.get(answer)

    return next_question


def check_rule(phone, rule):
    field, operation, expected = rule
    actual = phone.get(field)

    if actual is None or operation not in OPERATORS:
        return False

    try:
        return OPERATORS[operation](actual, expected)
    except (TypeError, ValueError):
        return False


def get_purpose(answers):
    if answers.get("work") is True:
        return "work"

    if answers.get("gaming") is True:
        return "gaming"

    if answers.get("photos") is True:
        if answers.get("videos") is True:
            return "video"
        return "photos"

    return "daily"


def calculate_score(phone, answers):
    score = 0

    for key, answer in answers.items():
        rule = rules.get(key, {}).get(answer)

        if rule is None:
            continue

        conditions = [rule] if isinstance(rule, tuple) else rule

        for condition in conditions:
            if check_rule(phone, condition):
                score += 3 if condition[0] == "purpose" else 2

    return score


def compare_features(phone, candidates, purpose):
    score = 0

    for field in PRIORITIES[purpose]:
        value = phone.get(field)

        if value is None:
            continue

        values = [
            other[field]
            for other in candidates
            if isinstance(other.get(field), (int, float, bool))
        ]

        if not values or max(values) == min(values):
            continue

        score += (value - min(values)) / (max(values) - min(values))

    return score


def recommend_phone(answers):
    budget = answers.get("budget")
    preferred_os = answers.get("os", "Без предпочитание")
    purpose = get_purpose(answers)

    candidates = [
        phone for phone in smartphones
        if (budget is None or phone["price"] <= budget)
        and (
            preferred_os in (None, "Без предпочитание")
            or phone["os"] == preferred_os
        )
    ]

    if not candidates:
        return None

    suitable = [
        phone for phone in candidates
        if purpose in phone.get("purpose", [])
    ]

    if suitable:
        candidates = suitable

    if budget is not None and budget >= 700:
        premium_candidates = [
            phone for phone in candidates
            if phone["price"] >= budget * 0.55
        ]

        if premium_candidates:
            candidates = premium_candidates

    return max(
        candidates,
        key=lambda phone: (
            calculate_score(phone, answers),
            compare_features(phone, candidates, purpose),
            -phone["price"],
            -phone["model_id"]
        )
    )
