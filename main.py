import numpy as np
import requests
from bs4 import BeautifulSoup
from utils import *
import webbrowser
import urllist

if __name__ == '__main__':
    COUNT = 1
    url = urllist.URL_list()

    elems = scray_all_page(url[0][0],url[0][1],COUNT)

    article_list = elems_to_list(elems,True)
    open_browser(article_list,True)


    elems = scray_all_page(url[1][0],url[1][1],COUNT)
    article_list2 = elems_to_list(elems,True)
