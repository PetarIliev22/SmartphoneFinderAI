from datetime import datetime, timezone

import pandas as pd
import requests
import streamlit as st

@st.cache_data(ttl=86400, show_spinner=False)
def get_phone_popularity(phone_name, region):
    params = {
        "engine": "google_trends",
        "q": phone_name,
        "date": "today 12-m",
        "data_type": "TIMESERIES",
        "api_key": st.secrets["SERPAPI_KEY"]
    }

    if region:
        params["geo"] = region

    response = requests.get(
        "https://serpapi.com/search.json",
        params=params,
        timeout=30
    )
    response.raise_for_status()

    result = response.json()

    if result.get("error"):
        raise ValueError(result["error"])

    timeline = result.get(
        "interest_over_time", {}
    ).get("timeline_data", [])

    records = []

    for item in timeline:
        values = item.get("values", [])
        timestamp = item.get("timestamp")

        if not values or timestamp is None:
            continue

        value = values[0].get("extracted_value")

        if value is not None:
            records.append({
                "Дата": datetime.fromtimestamp(
                    int(timestamp), tz=timezone.utc
                ),
                "Популярност": int(value)
            })

    return pd.DataFrame(records)

def show_popularity(phone):
    name = f"{phone['brand']} {phone['model']}"
    st.markdown("### Популярност на смартфона")

    try:
        with st.spinner("Зареждане на статистиката..."):
            data = get_phone_popularity(name, "BG")
            region = "България"

            if data.empty or data["Популярност"].max() == 0:
                data = get_phone_popularity(name, "")
                region = "Световна популярност"

        if data.empty or data["Популярност"].max() == 0:
            st.info("Няма достатъчно данни за популярността на този модел.")
            return

        st.caption(
            f"Интерес от Google търсения · {region} · Последните 12 месеца"
        )

        st.line_chart(
            data,
            x="Дата",
            y="Популярност",
            color="#ff4b4b",
            height=280
        )

        st.caption(
            "Относителен интерес от 0 до 100. "
            "Това не е статистика за продажби."
        )

    except requests.HTTPError as error:
        status = error.response.status_code

        if status == 429:
            st.warning("Достигнат е лимитът на API заявките.")
        elif status in (401, 403):
            st.warning("Проблем с API ключа или достъпа.")
        else:
            st.warning(f"Грешка от API: HTTP {status}")

    except (requests.RequestException, ValueError, KeyError) as error:
        st.warning(f"Неуспешно зареждане: {error}")
