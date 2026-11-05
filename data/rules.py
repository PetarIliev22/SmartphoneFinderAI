rules = {
    "work": {
        True: ("purpose", "contains", "work")
    },
    "documents": {
        True: ("storage", ">=", 256)
    },
    "gaming": {
        True: ("purpose", "contains", "gaming")
    },
    "photos": {
        True: ("purpose", "contains", "photos")
    },
    "many_apps": {
        True: ("ram", ">=", 12)
    },
    "heavy_games": {
        True: ("ram", ">=", 12)
    },
    "many_files": {
        True: ("storage", ">=", 256)
    },
    "large_games": {
        True: ("storage", ">=", 512)
    },
    "large_screen": {
        True: ("screen", ">=", 6.7)
    },
    "compact": {
        True: ("screen", "<=", 6.3)
    },
    "watch_videos": {
        True: ("screen", ">=", 6.7)
    },
    "outside": {
        True: ("battery", ">=", 5000)
    },
    "battery": {
        True: ("battery", ">=", 5500)
    },
    "long_gaming": {
        True: ("battery", ">=", 5500)
    },
    "videos": {
        True: ("purpose", "contains", "video")
    },
    "fast_charging": {
        True: ("charging_w", ">=", 45)
    },
    "wireless_charging": {
        True: ("wireless_charging", "==", True)
    },
    "high_refresh_rate": {
        True: ("refresh_rate", ">=", 120)
    },
    "video_4k_60": {
        True: ("video_4k_fps", ">=", 60)
    },
    "optical_zoom": {
        True: ("telephoto_optical_zoom", ">=", 3)
    },
    "ois": {
        True: ("ois", "==", True)
    }
}
