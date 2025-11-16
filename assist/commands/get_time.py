import datetime

def do_time(text):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    return f"Current time: {now}"
