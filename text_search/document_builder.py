from data.loader import smartphones, PURPOSE_TERMS

def build_document(phone):
    excluded = {"model_id", "image_url", "spec_source", "review_url", "youtube_url", "price"}

    document = []

    for key, value in phone.items():
        if key in excluded or value is None:
            continue

        if key == "purpose":
            value = ", ".join(
                PURPOSE_TERMS.get(p, p) for p in value
            )

        document.append(f"{key} {value}")

    return ", ".join(document)

def build_documents():
    return [build_document(phone) for phone in smartphones]

