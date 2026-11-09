import streamlit as st

from pathlib import Path
from text_search.ranking import recommend_phone, explain_phone

def show_phone_card(phone, index):
    with st.container(border=True, key=f"phone_card_{index}"):
        image = phone.get("image_url")

        if image and Path(image).is_file():
            st.image(image, width=300)

        st.markdown(
            f"**{phone['brand']} {phone['model']} — {phone['price']} €**"
        )

        if st.button(
            "Виж подробности →",
            key=f"details_{index}",
            use_container_width=True
        ):
            st.session_state.selected_chat_phone = phone
            st.session_state.page = "result"
            st.rerun()

def show_chat():
    with st.container(key="chat_container"):
        st.markdown("### Твоят AI асистент")
        st.caption("Опиши какъв смартфон търсиш.")

        st.session_state.setdefault("chat_messages", [
            {
                "role": "assistant",
                "content": (
                    "Здравей! 👋\n\n"
                    "Опиши ми какъв телефон търсиш "
                    "и за какво ще го използваш."
                )
            }
        ])

        with st.container(key="chat_messages"):
            for index, message in enumerate(st.session_state.chat_messages):
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

                    if phone := message.get("phone"):
                        show_phone_card(phone, index)

        prompt = st.chat_input(
            "Напиши какъв смартфон търсиш...",
            key="phone_chat_input"
        )

        if not prompt:
            return

        phone = recommend_phone(prompt)
        st.session_state.chat_recommendation_text = prompt

        st.session_state.chat_messages.append({
            "role": "user",
            "content": prompt
        })

        response = (
            f"📱 Препоръчвам ти **{phone['brand']} {phone['model']}**.\n\n"
            f"{explain_phone(phone, prompt)}"
            if phone else
            "Можеш ли да ми дадеш малко повече информация?\n\n"
            "Например какъв е бюджетът ти и за какво "
            "ще използваш смартфона?"
        )

        st.session_state.chat_messages.append({
            "role": "assistant",
            "content": response,
            "phone": phone
        })

        st.rerun()
