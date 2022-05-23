import requests
from bs4 import BeautifulSoup

def crawler():
    url = "https://gesetze.berlin.de/bsbe/document/MWRE220005943"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    items = soup
    
    return items

print(crawler())
