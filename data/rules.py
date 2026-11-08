rules = {
    "work": {
        True: ("purpose", "contains", "work")
    },
    "gaming": {
        True: ("purpose", "contains", "gaming")
    },
    "photos": {
        True: ("purpose", "contains", "photos")
    },
    "videos": {
        True: ("purpose", "contains", "video")
    },
    "daily": {
        True: ("purpose", "contains", "daily")
    },
    "documents": {
        True: ("storage", ">=", 256)
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
    "low_ram": {
        True: ("ram", "<=", 8)
    },
    "high_ram": {
        True: ("ram", ">=", 12)
    },
    "low_storage": {
        True: ("storage", "<=", 128)
    },
    "high_storage": {
        True: ("storage", ">=", 256)
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
    "small_battery": {
        True: ("battery", "<=", 4500)
    },
    "large_battery": {
        True: ("battery", ">=", 5500)
    },

    "fast_charging": {
        True: ("charging_w", ">=", 45)
    },
    "slow_charging": {
        True: ("charging_w", "<=", 25)
    },
    "wireless_charging": {
        True: ("wireless_charging", "==", True)
    },
    "high_refresh_rate": {
        True: ("refresh_rate", ">=", 120)
    },
    "low_refresh_rate": {
        True: ("refresh_rate", "<=", 60)
    },

    "high_camera_resolution": {
        True: ("camera", ">=", 50)
    },
    "low_camera_resolution": {
        True: ("camera", "<=", 48)
    },
    "ois": {
        True: ("ois", "==", True)
    },
    "optical_zoom": {
        True: ("telephoto_optical_zoom", ">=", 3)
    },
    "ultrawide_camera": {
        True: ("ultrawide_mp", ">=", 12)
    },

    "video_4k_60": {
        True: ("video_4k_fps", ">=", 60)
    },
    "video_8k": {
        True: ("video_8k_fps", ">=", 24)
    },
    "video_prores": {
        True: ("video_prores", "==", True)
    }
}
