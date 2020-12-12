# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 03:20:56 2020

@author: Eva
"""

import requests as re
from bs4 import BeautifulSoup

product =  input("請問想在博客來搜尋什麼?")


for k in range(3):
    if k == 0:
        url = "https://search.books.com.tw/search/query/key/" + product +"/cat/all"
    elif k == 1:
        url = "https://search.books.com.tw/search/query/cat/all/key/"+ product +"/sort/1/ms2/ms2_1/page/2/v/0/"
    else:
        url = "https://search.books.com.tw/search/query/cat/all/key/"+ product +"/sort/1/ms2/ms2_1/page/3/v/0/"
    
    r = re.request( "GET" , url)
    sp = BeautifulSoup( r.text , "html.parser" )
    
    if sp.find("div" ,class_="mod none") == None:
        books = sp.find_all("li",class_="item")
        book_name = []
        public = []
        price = []
        
        for i in books:
            book_name.append(i.find("h3").select('a')[0].get('title'))
            if i.find("a",rel="mid_publish") != None:
                public.append(i.find("a",rel="mid_publish").text)
            else:
                public.append(i.find("a",rel="mid_publish_ms2_6").text) 
            if len(i.find("span", class_ = "price").find_all("b")) > 1:
                price.append( i.find("span", class_ = "price").find_all("b")[1].text )
            else:
                price.append( i.find("span", class_ = "price").find_all("b")[0].text )
        authors = [[] for i in range(len(book_name))]
        
        
        for i in range(len(books)):
            author = books[i].find_all("a",rel="go_author")
            if(len(author) == 0):
                author = books[i].find_all("a",rel="go_author_ms2_6")  
            for j in author:
                authors[i].append(j.text)
        #print(price)
        
        
        
        
        for i in range(len(book_name)):
            print("書名:\t"+book_name[i])
            print("作者:\t")
            for j in authors[i]:
                print("\t"+j)
            print("出版社:\t"+public[i])
            print("價錢:\t"+price[i])
            print("\n")
            
    else:
        if k == 0:
            print("抱歉，找不到您所查詢的" + product + "資料")
            break
            
        