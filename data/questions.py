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
        "text": "Ще използвате ли смартфона често навън, без възможност за зареждане?",
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
        "next": 18
    },
    11: {
        "key": "large_screen",
        "text": "Предпочитате ли по-голям дисплей за четене и работа?",
        "type": "boolean",
        "next": 19
    },
    12: {
        "key": "battery",
        "text": "Важно ли е смартфонът да издържа цял ден без зареждане?",
        "type": "boolean",
        "next": 20
    },
    13: {
        "key": "compact",
        "text": "Предпочитате ли компактен смартфон?",
        "type": "boolean",
        "next": 21
    },
    14: {
        "key": "large_games",
        "text": "Ще инсталирате ли много игри, които заемат голямо пространство?",
        "type": "boolean",
        "next": 22
    },
    15: {
        "key": "long_gaming",
        "text": "Ще играете ли продължително време без зареждане?",
        "type": "boolean",
        "next": 23
    },
    16: {
        "key": "videos",
        "text": "Ще записвате ли често видеоклипове?",
        "type": "boolean",
        "next": {True: 24, False: 25}
    },
    17: {
        "key": "watch_videos",
        "text": "Ще гледате ли често филми и видеа?",
        "type": "boolean",
        "next": 26
    },
    18: {
        "key": "fast_charging",
        "text": "Важно ли е смартфонът да се зарежда бързо?",
        "type": "boolean",
        "next": 27
    },
    19: {
        "key": "high_refresh_rate",
        "text": "Важно ли е превъртането на текст и приложения да изглежда по-плавно?",
        "type": "boolean",
        "next": 28
    },
    20: {
        "key": "fast_charging",
        "text": "Важно ли е да можете да заредите телефона бързо, когато имате възможност?",
        "type": "boolean",
        "next": 29
    },
    21: {
        "key": "high_refresh_rate",
        "text": "Държите ли на по-плавна работа на дисплея?",
        "type": "boolean",
        "next": 30
    },
    22: {
        "key": "high_refresh_rate",
        "text": "Искате ли дисплей с висока честота на опресняване за по-плавни игри?",
        "type": "boolean",
        "next": 31
    },
    23: {
        "key": "high_refresh_rate",
        "text": "Искате ли дисплей с висока честота на опресняване за по-плавни игри?",
        "type": "boolean",
        "next": 32
    },
    24: {
        "key": "video_4k_60",
        "text": "Важно ли е да записвате 4K видео с 60 кадъра в секунда?",
        "type": "boolean",
        "next": 33
    },
    25: {
        "key": "optical_zoom",
        "text": "Важно ли е да приближавате отдалечени обекти с оптичен зуум?",
        "type": "boolean",
        "next": 34
    },
    26: {
        "key": "high_refresh_rate",
        "text": "Искате ли дисплей с по-плавно превъртане и анимации?",
        "type": "boolean",
        "next": 35
    },
    27: {
        "key": "wireless_charging",
        "text": "Важно ли е безжичното зареждане?",
        "type": "boolean",
        "next": None
    },
    28: {
        "key": "wireless_charging",
        "text": "Важно ли е безжичното зареждане?",
        "type": "boolean",
        "next": None
    },
    29: {
        "key": "wireless_charging",
        "text": "Бихте ли искали възможност за безжично зареждане?",
        "type": "boolean",
        "next": None
    },
    30: {
        "key": "wireless_charging",
        "text": "Важно ли е безжичното зареждане?",
        "type": "boolean",
        "next": None
    },
    31: {
        "key": "fast_charging",
        "text": "Искате ли бързо зареждане между игровите сесии?",
        "type": "boolean",
        "next": None
    },
    32: {
        "key": "fast_charging",
        "text": "Важно ли е бързото зареждане след продължителна игра?",
        "type": "boolean",
        "next": None
    },
    33: {
        "key": "ois",
        "text": "Важно ли е видеото да бъде по-стабилно при снимане от ръка?",
        "type": "boolean",
        "next": None
    },
    34: {
        "key": "ois",
        "text": "Снимате ли често от ръка и при по-слаба светлина?",
        "type": "boolean",
        "next": None
    },
    35: {
        "key": "fast_charging",
        "text": "Важно ли е бързото зареждане?",
        "type": "boolean",
        "next": None
    }
}
