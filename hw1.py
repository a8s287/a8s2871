# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 19:22:59 2020

@author: Eva
"""

import requests as re
import json

a = -1
while a != '0' and a != '1': 
    a = input( "請問你要借車(0)還是還車(1)" )
    if not(a == '1' or a == '0' ):
        print("請勿輸入不相關訊息")
    
b = input( "輸入中文場站區域" )

url = "https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f"
r = re.request( 'GET' , url ) #向url的網頁中request

jdata = json.loads( r.text ) #把request回來的網頁 從String轉成json格式ㄅ

flag = False
flag2 = False
if a == '0':
    for i in jdata['retVal']:
        if jdata['retVal'][i]['sarea'] == b: 
            flag = True     
            if int(jdata['retVal'][i]['sbi']) > 0 and int(jdata['retVal'][i]['act'])  == 1:
                print("序號:"+jdata['retVal'][i]['sno'])
                print("場站名稱:"+jdata['retVal'][i]['sna'])
                print("場站總停車格數:"+jdata['retVal'][i]['tot'])
                print("可借車位數:"+jdata['retVal'][i]['sbi'])
                print("地址:"+jdata['retVal'][i]['sarea']+jdata['retVal'][i]['ar'])
                print()
                flag2 = True
    if flag == False:
        print("並無可顯示的場站")
    else:
        if flag2 == False:
            print("該地區場站皆無可借車位")
  
    
flag = False
flag2 = False
if a == '1':
    for i in jdata['retVal']:
        if jdata['retVal'][i]['sarea'] == b: 
            flag = True     
            if int(jdata['retVal'][i]['bemp']) > 0 and int(jdata['retVal'][i]['act'])  == 1:
                print("序號:"+jdata['retVal'][i]['sno'])
                print("場站名稱:"+jdata['retVal'][i]['sna'])
                print("場站總停車格數:"+jdata['retVal'][i]['tot'])
                print("可還車位數:"+jdata['retVal'][i]['bemp'])
                print("地址:"+jdata['retVal'][i]['sarea']+jdata['retVal'][i]['ar'])
                print()
                flag2 = True
    if flag == False:
        print("並無可顯示的場站")
    else:
        if flag2 == False:
            print("該地區場站皆無可借車位")