import requests
from bs4 import BeautifulSoup

def scrape_stackoverflow_profile(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    name = soup.find("div", class_="user-card-name").text.strip()
    print("🧑 Name:", name)
