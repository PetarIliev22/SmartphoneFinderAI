
import streamlit as st


def show_header():
    st.html("""
        <div class="app-header">
            <h1 class="app-title">
                Твоят следващ смартфон.
                <span>Избран умно.</span>
            </h1>

            <p class="app-description">
                Отговори на няколко кратки въпроса и открий
                смартфона, който най-добре отговаря
                на бюджета и нуждите ти.
            </p>
        </div>
    """)
