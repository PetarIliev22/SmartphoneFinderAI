
rules = {
    "work": {
        True: ("purpose", "contains", "work")
    },

    "gaming": {
        True: ("purpose", "contains", "gaming")
    },

    "photos": {
        True: ("purpose", "contains", "photos"),
        False: ("purpose", "contains", "daily")
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

    "high_resolution_camera": {
        True: ("camera", ">=", 100)
    }
}
