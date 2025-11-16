import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as mic:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(mic, duration=0.3)

        try:
            audio = recognizer.listen(mic, timeout=5, phrase_time_limit=8)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            return ""
        except sr.WaitTimeoutError:
            return ""
        except Exception:
            return ""
