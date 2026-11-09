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
    
    st.segmented_control(
        "Режим",
        options=["analysis", "chat"],
        format_func=lambda x: {
            "analysis": "Подробен анализ",
            "chat": "AI Чат"
        }[x],
        default="analysis",
        key="mode",
        label_visibility="collapsed",
        width="stretch",
        required=True
    )
