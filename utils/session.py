
import streamlit as st

from data.questions import questions
from expert_system.recommender import get_next_question


def init_session():
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
