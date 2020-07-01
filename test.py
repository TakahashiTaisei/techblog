import requests
from bs4 import BeautifulSoup
import random
import webbrowser
import urllist


url = urllist.URL_list()



#次のページがある場合は再起的に記事を集めてくる関数を作るぞ

def scray_all_page(url:'request.get',tag:'article_tag',count:'int'):
    print("page:",count)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    elems = soup.find_all("a", class_=tag)
    count+=1
    next=soup.select('a[href*="page={}"]'.format(str(count)))
    print(next)
    if len(next)== 0:
        print("search last page")
        return elems
    print("url",next[0].get("href"))
    elems = elems + scray_all_page(next[0].get("href"),tag,count)
    return elems

count = 1
print(url[1][0],url[1][1])
elems = scray_all_page(url[1][0],url[1][1],count)

all_page = []
for e in elems:
  all_page.append([e.getText(),e.get("href")])
  print(e.getText(),e.get("href"))

rand = random.randint(0,len(all_page))
print("今日のおすすめ",all_page[rand])
print("(",len(all_page),"中)")
webbrowser.open_new(all_page[rand][1])

"""
elems = soup.find_all("a", class_="entry-title-link")
for e in elems:
  print(e.getText(),e.get("href"))

next=soup.select('a[href*="page={}"]'.format("2"))
#next = soup.find_all("a",{"class":"next"})
print(next[0].get("href"))
"""
