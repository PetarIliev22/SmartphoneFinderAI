import operator

from data.rules import rules
from data.loader import smartphones, PURPOSE_LABELS, FEATURE_LABELS
from data.questions import questions

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
    return next_question.get(answer) if isinstance(next_question, dict) else next_question

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
    match answers:
        case {"work": True}:
            return "work"
        case {"gaming": True}:
            return "gaming"
        case {"photos": True, "videos": True}:
            return "video"
        case {"photos": True}:
            return "photos"
        case _:
            return "daily"

def get_conditions(answers):
    for key, answer in answers.items():
        rule = rules.get(key, {}).get(answer)

        if rule is not None:
            yield from [rule] if isinstance(rule, tuple) else rule

def calculate_score(phone, answers):
    score = 0

    for condition in get_conditions(answers):
        points = 3 if condition[0] == "purpose" else 2
        score += points if check_rule(phone, condition) else -points

    return score

def compare_features(phone, candidates, purpose):
    score = 0

    for field in PRIORITIES[purpose]:
        value = phone.get(field)

        if not isinstance(value, (int, float, bool)):
            continue

        values = [
            candidate[field]
            for candidate in candidates
            if isinstance(candidate.get(field), (int, float, bool))
        ]

        if values:
            minimum, maximum = min(values), max(values)

            if maximum > minimum:
                score += (value - minimum) / (maximum - minimum)

    return score

def filter_phones(answers):
    min_budget, max_budget = answers.get("budget", (0, 2000))
    preferred_os = answers.get("os", "Без предпочитание")

    return [
        phone for phone in smartphones
        if min_budget <= phone["price"] <= max_budget
        and preferred_os in (None, "Без предпочитание", phone["os"])
    ]

def filter_requirements(candidates, answers):
    purpose = get_purpose(answers)

    suitable = [
        phone for phone in candidates
        if purpose in phone.get("purpose", [])
    ]

    if suitable:
        candidates = suitable

    requirements = [
        condition for condition in get_conditions(answers)
        if condition[0] != "purpose"
    ]

    matching = [
        phone for phone in candidates
        if all(check_rule(phone, req) for req in requirements)
    ]

    return matching or candidates

def recommend_phone(answers):
    candidates = filter_phones(answers)

    if not candidates:
        return None

    candidates = filter_requirements(candidates, answers)
    purpose = get_purpose(answers)

    return max(
        candidates,
        key=lambda phone: (
            calculate_score(phone, answers),
            compare_features(phone, candidates, purpose),
            -phone["price"],
            -phone["model_id"]
        )
    )

def explain_recommendation(phone, answers):
    purpose = get_purpose(answers)
    matched = []

    for condition in get_conditions(answers):
        field = condition[0]

        if field in FEATURE_LABELS and check_rule(phone, condition):
            label = FEATURE_LABELS[field]

            if label not in matched:
                matched.append(label)

    if purpose in phone.get("purpose", []):
        text = f"Този модел е подходящ за {PURPOSE_LABELS[purpose]}."
    else:
        text = "Този модел е най-близкото съответствие на вашите изисквания."

    if matched:
        text += " Основните му предимства са " + ", ".join(matched) + "."

    return text
