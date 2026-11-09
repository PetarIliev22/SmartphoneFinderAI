from html import escape
from pathlib import Path

import streamlit as st

from text_search.ranking import explain_phone
from expert_system.recommender import recommend_phone, explain_recommendation
from utils.popularity import show_popularity
from utils.session import restart

def render_specs(specifications):
    cards = "".join(
        f"""
        <div class="spec-card">
            <div class="spec-label">{escape(str(label))}</div>
            <div class="spec-value">{escape(str(value))}</div>
        </div>
        """
        for label, value in specifications
        if value is not None
    )

    if cards:
        st.html(f'<div class="spec-grid">{cards}</div>')

def add_spec(specifications, phone, key, label, unit=""):
    value = phone.get(key)

    if value is None:
        return

    if isinstance(value, bool):
        value = "Да" if value else "Не"
    elif unit:
        value = f"{value} {unit}"

    specifications.append((label, value))

def show_phone_specs(phone):
    specifications = [
        ("Операционна система", phone["os"]),
        ("RAM", f"{phone['ram']} GB"),
        ("Памет", f"{phone['storage']} GB"),
        ("Дисплей", f"{phone['screen']} инча"),
        ("Батерия", f"{phone['battery']} mAh"),
        ("Основна камера", f"{phone['camera']} MP")
    ]

    st.markdown("### Основни характеристики")
    render_specs(specifications)

    extra_specs = [
        ("chipset", "Процесор", ""),
        ("refresh_rate", "Честота на дисплея", "Hz"),
        ("charging_w", "Бързо зареждане", "W"),
        ("wireless_charging", "Безжично зареждане", ""),
        ("foldable", "Сгъваем дисплей", "")
    ]

    camera_specs = [
        ("ois", "Оптична стабилизация", ""),
        ("telephoto_optical_zoom", "Оптичен зуум", "x"),
        ("ultrawide_mp", "Ултраширока камера", "MP"),
        ("video_4k_fps", "4K видеозапис", "fps"),
        ("video_8k_fps", "8K видеозапис", "fps"),
        ("video_log", "Log видео", ""),
        ("video_prores", "ProRes видео", "")
    ]

    for title, fields in [
        ("Допълнителни характеристики", extra_specs),
        ("Камера и видео", camera_specs)
    ]:
        specs = []

        for key, label, unit in fields:
            add_spec(specs, phone, key, label, unit)

        if specs:
            st.markdown(f"### {title}")
            render_specs(specs)

def show_reviews(phone):
    review_url = phone.get("review_url")
    youtube_url = phone.get("youtube_url")
    spec_source = phone.get("spec_source")

    if not any((review_url, youtube_url, spec_source)):
        return

    st.divider()
    st.markdown("### Ревю и допълнителна информация")

    with st.container(key="review_section"):
        if review_url:
            st.markdown("#### Ревю на смартфона")
            st.caption(
                "Подробен преглед на дизайна, камерата, "
                "производителността и батерията."
            )
            st.link_button(
                "Прочети ревюто",
                review_url,
                icon=":material/open_in_new:",
                use_container_width=True,
                key="review_button"
            )

        if youtube_url:
            if review_url:
                st.divider()

            st.markdown("#### Видео ревю")
            st.caption("Видео представяне и тест на смартфона.")
            st.video(youtube_url)

        if spec_source:
            if review_url or youtube_url:
                st.divider()

            st.markdown("#### Пълни спецификации")
            st.caption(
                "Подробна информация за всички технически "
                "характеристики на модела."
            )
            st.link_button(
                "Виж спецификациите",
                spec_source,
                icon=":material/description:",
                use_container_width=True,
                key="specs_button"
            )

def show_result(phone=None, from_chat=False):
    if phone is None:
        phone = recommend_phone(st.session_state.answers)

    with st.container(key="result_card"):
        if phone is None:
            st.warning("Не открихме подходящ смартфон.")
        else:
            st.success(
                f"Препоръчваме: {phone['brand']} {phone['model']}"
            )

            image = phone.get("image_url")

            if image and (
                image.startswith(("http://", "https://"))
                or Path(image).is_file()
            ):
                with st.container(key="phone_image"):
                    st.image(image, width="stretch")

            st.markdown(f"## Цена: {phone['price']} €")

            if from_chat:
                explanation = explain_phone(
                    phone,
                    st.session_state.get("chat_recommendation_text", "")
                )
            else:
                explanation = explain_recommendation(
                    phone,
                    st.session_state.answers
                )

            st.warning(
                f"**Защо избрахме този смартфон?**\n\n{explanation}"
            )

            show_phone_specs(phone)
            show_reviews(phone)

            st.divider()
            show_popularity(phone)

        st.divider()

        if st.button(
            "Започни отначало",
            type="primary",
            use_container_width=True,
            key="restart_button"
        ):
            restart()
            st.session_state.page = "chat" if from_chat else "analysis"
            st.session_state.mode = st.session_state.page
            st.session_state.selected_chat_phone = None
            st.rerun()
