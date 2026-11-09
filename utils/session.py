import streamlit as st

from data.questions import questions
from expert_system.recommender import get_next_question

def init_session():
    st.session_state.setdefault("answers", {})
    st.session_state.setdefault("question_id", 1)

def save_answer(answer):
    question_id = st.session_state.question_id

    st.session_state.answers[questions[question_id]["key"]] = answer
    st.session_state.question_id = get_next_question(question_id, answer)

def restart():
    st.session_state.answers = {}
    st.session_state.question_id = 1
