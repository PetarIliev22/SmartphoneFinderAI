
import streamlit as st


def show_header():
    st.html("""
        <div class="app-header">
            <div class="app-eyebrow">
                SMARTPHONE FINDER
            </div>

            <h1 class="app-title">
                Открий своя
                <span class="app-title-accent">идеален смартфон.</span>
            </h1>

            <p class="app-description">
                Отговори на няколко кратки въпроса.
                Ние ще подберем най-подходящия смартфон
                според твоя бюджет и нужди.
            </p>
        </div>
    """)
