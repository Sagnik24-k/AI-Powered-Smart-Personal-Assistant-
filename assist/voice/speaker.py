import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 185)     # Speed
engine.setProperty("volume", 0.9)   # Loudness

def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()
