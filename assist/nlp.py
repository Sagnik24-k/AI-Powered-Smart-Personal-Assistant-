from difflib import get_close_matches

INTENTS = {
    "calculate": ["calculate", "calc", "compute", "solve"],
    "weather": ["weather", "temperature", "forecast"],
    "time": ["time", "current time", "what time"],
    "open": ["open", "launch", "start"],
    "search": ["search", "google"],
    "smalltalk": ["hi", "hello", "how are you", "who are you"]
}

def detect_intent(text):
    text = text.lower()

    for intent, words in INTENTS.items():
        for w in words:
            if w in text:
                return intent

    all_words = sum(INTENTS.values(), [])
    close = get_close_matches(text, all_words, n=1, cutoff=0.6)
    if close:
        for intent, words in INTENTS.items():
            if close[0] in words:
                return intent

    return "unknown"
