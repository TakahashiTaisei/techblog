import requests
from bs4 import BeautifulSoup

url = "https://techblog.zozo.com/archive/2020"
article_tag = "entry-title-link"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

"""
for aa in soup.find_all("a"):
            link = aa.get("href")
            name = aa.get_text()
            print(link,"\t",name)
"""

#次のページがある場合は再起的に記事を集めてくる関数を作るぞ
def scray_all_page(url:'request.get',count:'int'):
    print("page:",count)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    elems = soup.find_all("a", class_=article_tag)
    count+=1
    next=soup.select('a[href*="page={}"]'.format(str(count)))
    print(next)
    if len(next)== 0:
        print("search last page")
        return elems
    print("url",next[0].get("href"))
    elems = elems + scray_all_page(next[0].get("href"),count)
    return elems
count = 1
elems = scray_all_page(url,count)

for e in elems:
  print(e.getText(),e.get("href"))

"""
elems = soup.find_all("a", class_="entry-title-link")
for e in elems:
  print(e.getText(),e.get("href"))

next=soup.select('a[href*="page={}"]'.format("2"))
#next = soup.find_all("a",{"class":"next"})
print(next[0].get("href"))
"""
