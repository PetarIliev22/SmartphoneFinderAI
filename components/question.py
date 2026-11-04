
import streamlit as st

from data.questions import questions
from utils.session import save_answer


def show_question():
    question = questions[st.session_state.question_id]
    step = len(st.session_state.answers) + 1

    show_steps(step)

    with st.container(border=True, key="question_card"):
        st.markdown(f"### {question['text']}")

        if question["type"] == "boolean":
            st.caption("Изберете един от двата отговора.")

            yes, no = st.columns(2, gap="small")

            with yes:
                if st.button(
                    "Да",
                    type="primary",
                    use_container_width=True,
                    key="yes"
                ):
                    save_answer(True)
                    st.rerun()

            with no:
                if st.button(
                    "Не",
                    use_container_width=True,
                    key="no"
                ):
                    save_answer(False)
                    st.rerun()

        elif question["type"] == "number":
            budget = st.number_input(
                "Максимален бюджет (€)",
                min_value=0,
                value=500,
                step=50
            )

            if st.button(
                "Продължи",
                type="primary",
                use_container_width=True
            ):
                save_answer(budget)
                st.rerun()

        elif question["type"] == "choice":
            choice = st.radio(
                "Операционна система",
                question["options"]
            )

            if st.button(
                "Продължи",
                type="primary",
                use_container_width=True
            ):
                save_answer(choice)
                st.rerun()


def show_steps(current, total=6):
    steps = '<div class="steps">'

    for i in range(1, total + 1):
        active = "active" if i == current else ""

        steps += f'<div class="step {active}">{i}</div>'

        if i < total:
            steps += '<div class="step-line"></div>'

    steps += '</div>'

    st.html(steps)
