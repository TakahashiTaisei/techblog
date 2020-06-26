import requests
import bs4 import BeautifulSoup

url = "https://techblog.zozo.com"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

elems = soup.find_all("a", class_="reference internal")
for e in elems:
  print(e.getText())
