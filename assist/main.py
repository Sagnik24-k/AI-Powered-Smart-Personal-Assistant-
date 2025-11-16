from nlp import detect_intent

from voice.listener import listen
from voice.speaker import speak

from commands.calculate import do_calculate
from commands.weather import do_weather
from commands.get_time import do_time
from commands.open_app import do_open
from commands.search import do_search
from commands.smalltalk import do_smalltalk

def run_voice_bot():
    speak("Voice assistant activated. How can I help?")

    while True:
        user = listen()
        if not user:
            continue

        if "exit" in user or "stop" in user or "bye" in user:
            speak("Goodbye.")
            break

        intent = detect_intent(user)

        if intent == "calculate":
            speak(do_calculate(user))
        elif intent == "weather":
            speak(do_weather(user))
        elif intent == "time":
            speak(do_time(user))
        elif intent == "open":
            speak(do_open(user))
        elif intent == "search":
            speak(do_search(user))
        elif intent == "talk":
            speak(do_smalltalk(user))
        else:
            speak("I didn't get that.")

if __name__ == "__main__":
    run_voice_bot()
