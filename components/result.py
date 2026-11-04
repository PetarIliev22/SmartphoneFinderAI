
import streamlit as st
from html import escape

from recommender import recommend_phone
from utils.session import restart


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

            if phone.get("image_url"):
                st.image(phone["image_url"], width=250)

            st.markdown(f"## Цена: {phone['price']} €")
            specifications = [
                ("Операционна система", phone["os"]),
                ("RAM", f"{phone['ram']} GB"),
                ("Памет", f"{phone['storage']} GB"),
                ("Дисплей", f"{phone['screen']} инча"),
                ("Батерия", f"{phone['battery']} mAh"),
                ("Камера", f"{phone['camera']} MP")
            ]

            cards = "".join(
                f"""
                <div class="spec-card">
                    <div class="spec-label">{escape(str(label))}</div>
                    <div class="spec-value">{escape(str(value))}</div>
                </div>
                """
                for label, value in specifications
            )

            st.html(f'<div class="spec-grid">{cards}</div>')

    if st.button(
        "Започни отначало",
        type="primary",
        use_container_width=True,
        key="restart_button"
    ):
        restart()
        st.rerun()
