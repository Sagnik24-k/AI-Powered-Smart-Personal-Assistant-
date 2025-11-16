import re

def do_calculate(text):
    expression = re.sub("[^0-9+\-*/().]", "", text)
    try:
        result = eval(expression)
        return f"Result: {result}"
    except:
        return "Invalid expression."
