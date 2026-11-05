
import streamlit as st
from pathlib import Path
import base64
from utils.session import init_session
from components.header import show_header
from components.question import show_question
from components.result import show_result

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

    if st.session_state.question_id is not None:
        show_header()
        show_question()
    else:
        show_result()


if __name__ == "__main__":
    main()
