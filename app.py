
import streamlit as st

from data.questions import questions
from recommender import get_next_question, recommend_phone


st.set_page_config(
    page_title="Препоръчване на смартфони",
)

st.title("Система за препоръчване на смартфони")

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "question_id" not in st.session_state:
    st.session_state.question_id = 1


def save_answer(answer):
    question_id = st.session_state.question_id
    question = questions[question_id]

    st.session_state.answers[question["key"]] = answer
    st.session_state.question_id = get_next_question(
        question_id, answer
    )


def restart():
    st.session_state.answers = {}
    st.session_state.question_id = 1


question_id = st.session_state.question_id

if question_id is not None:
    question = questions[question_id]

    st.subheader(question["text"])

    if question["type"] == "boolean":
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Да", use_container_width=True):
                save_answer(True)
                st.rerun()

        with col2:
            if st.button("Не", use_container_width=True):
                save_answer(False)
                st.rerun()

    elif question["type"] == "number":
        budget = st.number_input(
            "Бюджет (€)",
            min_value=0,
            value=500,
            step=50
        )

        if st.button("Продължи", use_container_width=True):
            save_answer(budget)
            st.rerun()

    elif question["type"] == "choice":
        choice = st.radio(
            "Изберете вариант:",
            question["options"]
        )

        if st.button("Продължи", use_container_width=True):
            save_answer(choice)
            st.rerun()

else:
    phone = recommend_phone(st.session_state.answers)

    st.subheader("Резултат")

    if phone:
        st.success(f"Препоръчваме: {phone['brand']} {phone['model']}")

        st.write(f"**Цена:** {phone['price']} €")
        st.write(f"**Операционна система:** {phone['os']}")
        st.write(f"**RAM:** {phone['ram']} GB")
        st.write(f"**Памет:** {phone['storage']} GB")
        st.write(f"**Дисплей:** {phone['screen']} инча")
        st.write(f"**Батерия:** {phone['battery']} mAh")
        st.write(f"**Камера:** {phone['camera']} MP")
    else:
        st.warning(
            "Няма смартфон в зададения бюджет "
            "и с избраната операционна система."
        )

    if st.button("Започни отначало", use_container_width=True):
        restart()
        st.rerun()
