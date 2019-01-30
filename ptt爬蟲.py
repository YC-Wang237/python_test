# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:36:18 2019

@author: YUNG-CHUN
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/joke/index.html"
for i in range(2): #爬2頁
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"lxml")
    u = soup.select("div.btn-group.btn-group-paging a") 
    for entry in soup.select('.r-ent'):
        for s in entry.select('div.title a'):
            entry_url = "https://www.ptt.cc"+s['href']
            entry_res = requests.get(entry_url)
            entry_soup = BeautifulSoup(entry_res.text,"html.parser")
            main_content = entry_soup.find(id="main-content")
            metas = main_content.select('div.article-metaline')
            filtered = [ v for v in main_content.stripped_strings if v[0] not in [u'※', u'◆'] and  v[:2] not in [u'--'] ]
            author = filtered[1]
            title = filtered[5]
            date = filtered[7]
            tag = filtered[3]
            content = filtered[8]
            print("日期: "+date+"\n"+"作者: "+author+"\n"+"標題: "+title+"\n"+"內容:\n"+content+"\n\n"+"看板名稱: "+tag+"\n")
    url = "https://www.ptt.cc"+ u[1]["href"] #上一頁


