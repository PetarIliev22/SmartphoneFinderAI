
import streamlit as st

from data.questions import questions
from utils.session import save_answer


def show_question():
    question = questions[st.session_state.question_id]
    step = len(st.session_state.answers) + 1

    with st.container(key="question_card"):
        show_steps(step)
        st.markdown(f"### {question['text']}")

        if question["type"] == "boolean":
            st.caption("Изберете един от двата отговора.")

            yes, no = st.columns(2, gap="small")

            with yes:
                if st.button("Да", type="primary", use_container_width=True):
                    submit_answer(True)

            with no:
                if st.button("Не", use_container_width=True):
                    submit_answer(False)

        elif question["type"] == "number":
            budget = st.slider(
                "Изберете ценови диапазон (€)",
                min_value=0,
                max_value=2000,
                value=(350, 750),
                step=50,
                on_change="ignore"
            )

            if st.button("Продължи", type="primary", use_container_width=True):
                submit_answer(budget)

        elif question["type"] == "choice":
            choice = st.radio("Операционна система", question["options"])

            if st.button("Продължи", type="primary", use_container_width=True):
                submit_answer(choice)

def submit_answer(answer):
    save_answer(answer)
    st.rerun()

def show_steps(current, total=8):
    elements = []

    for i in range(1, total + 1):
        active = "active" if i == current else ""
        elements.append(f'<div class="step {active}">{i}</div>')

        if i < total:
            elements.append('<div class="step-line"></div>')

    st.html(f'<div class="steps">{"".join(elements)}</div>')
