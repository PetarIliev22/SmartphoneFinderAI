import streamlit as st
from pathlib import Path
import base64
from utils.session import init_session
from components.header import show_header
from components.question import show_question
from components.result import show_result
from components.chat import show_chat

def main():
    bg_path = Path(__file__).parent / "assets/bg/background.png"
    bg_base64 = base64.b64encode(bg_path.read_bytes()).decode()

    st.markdown(
        f"<style>.stApp {{ background-image: url('data:image/png;base64,{bg_base64}'); }}</style>",
        unsafe_allow_html=True
    )
    
    st.set_page_config(
        page_title="Препоръчване на смартфони",
        layout="centered"
    )

    css = Path(__file__).parent / "styles" / "style.css"
    
    st.markdown(
        f"<style>{css.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True
    )

    init_session()

    if "page" not in st.session_state:
        st.session_state.page = "analysis"

    if "mode" not in st.session_state:
        st.session_state.mode = "analysis"

    if st.session_state.page != "result":
        show_header()

        st.segmented_control(
            "Режим",
            options=["analysis", "chat"],
            format_func=lambda x: {
                "analysis": "Подробен анализ",
                "chat": "AI Чат"
            }[x],
            key="mode",
            label_visibility="collapsed",
            width="stretch"
        )

        st.session_state.page = st.session_state.mode

    match st.session_state.page:
        case "chat":
            show_chat()

        case "analysis":
            if st.session_state.question_id is not None:
                show_question()
            else:
                show_result()

        case "result":
            show_result(
                st.session_state.selected_chat_phone,
                from_chat=True
            )

if __name__ == "__main__":
    main()
