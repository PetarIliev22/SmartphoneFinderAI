from data.loader import smartphones

def build_document(phone):
    excluded = {"model_id", "image_url", "spec_source", "review_url", "youtube_url", "price"}
    return ", ".join(f"{key} {value}" for key, value in phone.items()  if key not in excluded and value is not None)

def build_documents():
    return [build_document(phone) for phone in smartphones]
    #  *EXAMPLE OUTPUT* 
    # * brand Samsung , model Galaxy A35 , os Android , ram 6 , storage 128 , screen 6.6 , battery 5000 , camera 50 , purpose ['daily'] , refresh_rate 120 , charging_w 25 , wireless_charging False , video_4k_fps 30 , ois True , ultrawide_mp 8

