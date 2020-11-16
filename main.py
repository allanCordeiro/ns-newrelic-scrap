from bs4 import BeautifulSoup
import requests

def new_relic_status():
    html = requests.get("https://status.newrelic.com/").content
    soup = BeautifulSoup(html, 'html.parser')
    system_status = soup.find("span", class_="system-text")

    if system_status.string == "All systems are working normally":
        return "OK"

    return "NOK"


if __name__ == "__main__":
    print(new_relic_status())