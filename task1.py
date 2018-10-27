# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
import datetime
from bs4 import BeautifulSoup
import requests
today = datetime.date.today()
date = today.strftime('%d-%m-%Y')
r = requests.get('http://stock.vietnammarkets.com/vietnam-stock-market.php')
html = r.text
lis = []
dic = {}
soup = BeautifulSoup(html, "lxml")
tables = soup.findChildren('table')
my_table = tables[0]
rows = my_table.findChildren(['th', 'tr'])
for row in rows:
    cells = row.findChildren('td')
    #print (cells)
    for cell in cells:
         #value = cell.string
         #print (value)
         for a in cell.find_all('a', href=True):
             url = (a['href'])
             dic = {"ticker symbol": cells[0].string, "company name": cells[1].string, "url" : url,
           "business": cells[2].string, "crawled_at" : date, "Listing bourse": cells[3].string}
        #print (cell)
    lis.append(dic)
js = json.dumps(lis)
fp = open('company_index.json', 'a')
fp.write(js)
fp.close()
