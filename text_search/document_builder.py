from data.loader import smartphones, PURPOSE_TERMS

EXCLUDED = {"model_id", "image_url", "spec_source", "review_url", "youtube_url", "price"}

def build_document(phone):
    document = []

    for key, value in phone.items():
        if key in EXCLUDED or value is None:
            continue

        if key == "purpose":
            value = ", ".join(PURPOSE_TERMS.get(p, p) for p in value)

        document.append(f"{key} {value}")

    return ", ".join(document)


def build_documents():
    return [build_document(phone) for phone in smartphones]
