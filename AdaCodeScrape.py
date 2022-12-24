import requests
from bs4 import BeautifulSoup
page = requests.get("https://xurlocation.com/ada-1-mods-today-destiny-2/")
soup = BeautifulSoup(page.content, 'html.parser')
weapons = soup.find_all('ul')[2]
weapons = weapons.text