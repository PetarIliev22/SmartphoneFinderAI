
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

def get_next_question(question_id, answer):
    next_question = questions[question_id]["next"]
    return next_question.get(answer) if isinstance(next_question, dict) else next_question


def check_rule(phone, rule):
    field, operation, value = rule
    return OPERATORS[operation](phone[field], value)

def calculate_score(phone, answers):
    score = 0

    for question in questions.values():
        key = question["key"]
        if key not in answers:
            continue

        rule = rules.get(key, {}).get(answers[key])
        if rule is None:
            continue

        for condition in ([rule] if isinstance(rule, tuple) else rule):
            if check_rule(phone, condition):
                score += 3 if condition[0] == "purpose" else 1

    return score

def recommend_phone(answers):
    budget = answers.get("budget")
    preferred_os = answers.get("os", "Без предпочитание")

    candidates = [
        phone for phone in smartphones
        if (budget is None or phone["price"] <= budget)
        and (preferred_os in (None, "Без предпочитание") or phone["os"] == preferred_os)
    ]

    return max(
        candidates,
        key=lambda phone: (calculate_score(phone, answers), -phone["price"]),
        default=None
    )