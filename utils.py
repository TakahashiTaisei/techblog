import requests
from bs4 import BeautifulSoup
import webbrowser
import random

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

def elems_to_list(elems:'elems',print_flag:'TRUE,FALSE'):
    all_page = []
    for e in elems:
        all_page.append([e.getText(),e.get("href")])
        if print_flag==True:
            print(e.getText(),e.get("href"))
    return all_page

def open_browser(article_list:'article_list',start:'True,False'):
    rand = random.randint(0,len(article_list)-1)
    print("今日のおすすめ",article_list[rand],"(",len(article_list),"中)")
    if start == True:
        webbrowser.open_new(article_list[rand][1])
