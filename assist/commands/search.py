import webbrowser

def do_search(text):
    query = (
        text.replace("search", "")
            .replace("google", "")
            .strip()
    )

    if not query:
        return "Tell me what to search."

    webbrowser.open(f"https://www.google.com/search?q={query}")
    return f"Searching: {query}"
