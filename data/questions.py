questions = {
    1: {
        "key": "budget",
        "text": "Каква е максималната сума, която сте готови да отделите за смартфон?",
        "type": "number",
        "next": 2
    },

    2: {
        "key": "os",
        "text": "Каква операционна система предпочитате?",
        "type": "choice",
        "options": ["Android", "iOS", "Без предпочитание"],
        "next": 3
    },

    3: {
        "key": "work",
        "text": "Ще използвате ли смартфона предимно за работа?",
        "type": "boolean",
        "next": {True: 4, False: 5}
    },

    4: {
        "key": "documents",
        "text": "Ще работите ли често с документи?",
        "type": "boolean",
        "next": {True: 6, False: 7}
    },

    5: {
        "key": "gaming",
        "text": "Ще използвате ли смартфона предимно за игри?",
        "type": "boolean",
        "next": {True: 8, False: 9}
    },

    6: {
        "key": "many_apps",
        "text": "Ще използвате ли няколко приложения едновременно?",
        "type": "boolean",
        "next": {True: 10, False: 11}
    },

    7: {
        "key": "outside",
        "text": "Ще използвате ли смартфона често извън офиса?",
        "type": "boolean",
        "next": {True: 12, False: 13}
    },

    8: {
        "key": "heavy_games",
        "text": "Ще играете ли игри с високи графични изисквания?",
        "type": "boolean",
        "next": {True: 14, False: 15}
    },

    9: {
        "key": "photos",
        "text": "Ще използвате ли смартфона предимно за снимки и видео?",
        "type": "boolean",
        "next": {True: 16, False: 17}
    },

    10: {
        "key": "many_files",
        "text": "Ще съхранявате ли много работни файлове?",
        "type": "boolean",
        "next": None
    },

    11: {
        "key": "large_screen",
        "text": "Предпочитате ли по-голям дисплей за четене и работа?",
        "type": "boolean",
        "next": None
    },

    12: {
        "key": "battery",
        "text": "Важно ли е смартфонът да издържа цял ден без зареждане?",
        "type": "boolean",
        "next": None
    },

    13: {
        "key": "compact",
        "text": "Предпочитате ли компактен смартфон?",
        "type": "boolean",
        "next": None
    },

    14: {
        "key": "large_games",
        "text": "Ще инсталирате ли много игри, които заемат голямо пространство?",
        "type": "boolean",
        "next": None
    },

    15: {
        "key": "long_gaming",
        "text": "Ще играете ли продължително време без зареждане?",
        "type": "boolean",
        "next": None
    },

    16: {
        "key": "videos",
        "text": "Ще записвате ли често видеоклипове?",
        "type": "boolean",
        "next": None
    },

    17: {
        "key": "watch_videos",
        "text": "Ще гледате ли често филми и видеа?",
        "type": "boolean",
        "next": None
    }
}
