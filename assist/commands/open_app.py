import subprocess

def do_open(text):
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    }

    for app, path in apps.items():
        if app in text:
            subprocess.Popen(path)
            return f"Opening {app}."

    return "App not mapped."
