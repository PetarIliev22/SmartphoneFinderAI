import base64
import streamlit as st

from pathlib import Path
from utils.session import init_session
from components.header import show_header
from components.question import show_question
from components.result import show_result
from components.chat import show_chat

def main():
    st.set_page_config(
        page_title="Препоръчване на смартфони",
        layout="centered"
    )

    root = Path(__file__).parent

    bg = base64.b64encode(
        (root / "assets/bg/background.png").read_bytes()
    ).decode()

    st.markdown(
        f"""
        <style>
        @media (max-width: 600px) {{
            .stApp {{
                background-image: url("data:image/png;base64,{bg}") !important;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    css = (root / "styles/style.css").read_text(encoding="utf-8")

    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

    init_session()

    if "page" not in st.session_state:
        st.session_state.page = "analysis"

    if "mode" not in st.session_state:
        st.session_state.mode = "analysis"

    is_result = (
        st.session_state.page == "result"
        or (
            st.session_state.page == "analysis"
            and st.session_state.question_id is None
        )
    )

    if not is_result:
        show_header()
        st.session_state.page = st.session_state.mode

    match st.session_state.page:
        case "chat":
            show_chat()

        case "analysis":
            if st.session_state.question_id is None:
                show_result()
            else:
                show_question()

        case "result":
            show_result(
                phone=st.session_state.selected_chat_phone,
                from_chat=True
            )


if __name__ == "__main__":
    main()
