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
        True: ("ram", ">=", 8)
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
        True: ("screen", ">=", 6.6)
    },

    "compact": {
        True: ("screen", "<=", 6.2)
    },

    "watch_videos": {
        True: ("screen", ">=", 6.6)
    },

    "outside": {
        True: ("battery", ">=", 4500)
    },

    "battery": {
        True: ("battery", ">=", 5000)
    },

    "long_gaming": {
        True: ("battery", ">=", 5000)
    },

    "videos": {
        True: ("purpose", "contains", "video")
    },

    "high_resolution_camera": {
        True: ("camera", ">=", 64)
    }
}
