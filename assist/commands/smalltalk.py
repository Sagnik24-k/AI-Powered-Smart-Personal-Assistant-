import random
import re
from utils.llm_client import ask_llm

BAD_WORDS = [
    "fuck", "fucking", "shit", "bitch", "bastard",
    "asshole", "dumbass", "motherfucker", "stfu",
    "idiot", "retard"
]

def contains_profanity(text):
    text = text.lower()
    return any(bad in text for bad in BAD_WORDS)


def do_smalltalk(text):
    text = text.lower()

    if contains_profanity(text):
        tone = random.choice([
            "annoyed",
            "unimpressed",
            "sarcastic",
            "cold"
        ])
        prompt = f"""
The user said: "{text}".

Reply in a short, sharp, annoyed tone. 
Do NOT be apologetic. Do NOT be soft.
Keep the reply under 15 words. No profanity in your answer.
"""
        return ask_llm(prompt)

    # Normal small talk using LLM
    prompt = f"""
Respond naturally to this message: "{text}".
Keep your answer:
- short (under 15 words)
- casual, confident
- NOT cringe
- NOT overly polite
"""

    return ask_llm(prompt)
