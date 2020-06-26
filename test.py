import requests
from bs4 import BeautifulSoup

url = "https://techblog.zozo.com/archive/2020"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

"""
for aa in soup.find_all("a"):
            link = aa.get("href")
            name = aa.get_text()
            print(link,"\t",name)
"""



elems = soup.find_all("a", class_="entry-title-link")
for e in elems:
  print(e.getText(),e.get("href"))
