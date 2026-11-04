
import streamlit as st

def show_header():
    st.html("""
        <div class="app-header">
            <h1 class="app-title">
                Намери подходящия
                <span class="app-title-second">смартфон за теб.</span>
            </h1>

            <p class="app-description">
                Отговори на няколко въпроса и получи
                препоръка според бюджета и начина,
                по който използваш телефона си.
            </p>
        </div>
    """)
