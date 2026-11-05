
import streamlit as st
from html import escape
from pathlib import Path
from utils.popularity import show_popularity
from recommender import recommend_phone
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


def show_result():
    phone = recommend_phone(st.session_state.answers)

    st.subheader("Резултат")

    if phone is None:
        st.warning(
            "Няма смартфон в зададения бюджет "
            "и с избраната операционна система."
        )
    else:
        with st.container(border=True, key="result_card"):
            st.success(
                f"Препоръчваме: {phone['brand']} {phone['model']}"
            )

            image = phone.get("image_url")

            if image:
                if image.startswith(("https://", "http://")):
                    st.image(image, width=250)
                elif Path(image).is_file():
                    st.image(image, width=500)


            st.markdown(f"## Цена: {phone['price']} €")
            st.markdown("### Основни характеристики")

            specifications = [
                ("Операционна система", phone["os"]),
                ("RAM", f"{phone['ram']} GB"),
                ("Памет", f"{phone['storage']} GB"),
                ("Дисплей", f"{phone['screen']} инча"),
                ("Батерия", f"{phone['battery']} mAh"),
                ("Основна камера", f"{phone['camera']} MP")
            ]

            render_specs(specifications)

            extra_specs = []

            add_spec(extra_specs, phone, "chipset", "Процесор")
            add_spec(extra_specs, phone, "refresh_rate", "Честота на дисплея", "Hz")
            add_spec(extra_specs, phone, "charging_w", "Бързо зареждане", "W")
            add_spec(extra_specs, phone, "wireless_charging", "Безжично зареждане")
            add_spec(extra_specs, phone, "foldable", "Сгъваем дисплей")

            if extra_specs:
                st.markdown("### Допълнителни характеристики")
                render_specs(extra_specs)

            camera_specs = []

            add_spec(camera_specs, phone, "ois", "Оптична стабилизация")
            add_spec(
                camera_specs,
                phone,
                "telephoto_optical_zoom",
                "Оптичен зуум",
                "x"
            )
            add_spec(
                camera_specs,
                phone,
                "ultrawide_mp",
                "Ултраширока камера",
                "MP"
            )
            add_spec(
                camera_specs,
                phone,
                "video_4k_fps",
                "4K видеозапис",
                "fps"
            )
            add_spec(
                camera_specs,
                phone,
                "video_8k_fps",
                "8K видеозапис",
                "fps"
            )
            add_spec(camera_specs, phone, "video_log", "Log видео")
            add_spec(camera_specs, phone, "video_prores", "ProRes видео")

            if camera_specs:
                st.markdown("### Камера и видео")
                render_specs(camera_specs)

            review_url = phone.get("review_url")
            youtube_url = phone.get("youtube_url")
            spec_source = phone.get("spec_source")

            if review_url or youtube_url:
                st.divider()
                st.markdown("### Ревю и видео")
                
                with st.container(border=True, key="review_section"):
                    st.markdown("**Текстово ревю**")
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
                        st.markdown("#### Видео ревю")
                        st.video(youtube_url)

                    if spec_source:
                        st.link_button(
                            "Виж пълните спецификации",
                            spec_source,
                            icon=":material/description:",
                            use_container_width=True,
                            key="specs_button"
                        )
                
            st.divider()
            show_popularity(phone)

    if st.button(
        "Започни отначало",
        type="primary",
        use_container_width=True,
        key="restart_button"
    ):
        restart()
        st.rerun()
