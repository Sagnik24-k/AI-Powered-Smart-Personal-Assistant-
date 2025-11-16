from utils.scraper import get_soup
import re

def do_weather(text):
    try:
        location = "your city"
        match = re.search(r"in (.*)", text)
        if match:
            location = match.group(1)

        url = f"https://www.google.com/search?q=weather+{location}"
        soup = get_soup(url)

        temp = soup.find("span", attrs={"id": "wob_tm"}).text
        cond = soup.find("span", attrs={"id": "wob_dc"}).text

        return f"Weather in {location.title()}: {temp}°C, {cond}"
    except:
        return "Couldn't fetch weather."
