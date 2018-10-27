# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:57:12 2018

@author: Farid al rafi
"""


import json
import datetime
from bs4 import BeautifulSoup
import requests

def company_profile(url):
    r_2 = requests.get(url)

    soup_profile = BeautifulSoup(r_2.text, "lxml")
    tables = soup_profile.findChildren('table')
    
    
    my_table = tables[0]
    rows = my_table.findChildren(['th', 'tr'])
    
    cell0 = rows[0].findChildren('td')
    cell=cell0[0]  #company profile row 1
    result = cell.find_all(text=True)
    #print(result)
    title = soup_profile.title.string 
    title = title.split(':') 
    ticker_symbol = title[0]
    company_name = title[1]#result[1].string
    company_address = result[2].string
    company_phone_num = [result[3].string.strip('\t,\n '),result[4].string.strip('\t,\n ')]
    industry = result[7].string.split(':') 
    company_industry = industry[1]
    company_website = str(result[6].string)
    company_email = str(result[5].string)
    financial_table = (cell0[1].findChildren('table'))
    financial_sum = financial_table[0]
    financial_sum_result=(financial_sum.find_all('td'))
    financial_summary = {"capital_curency": financial_sum_result[1].string, "market_cap" : financial_sum_result[3].string,
                         "par_value": financial_sum_result[5].string, "equity": financial_sum_result[7].string,
                         "listing_volume": financial_sum_result[9].string, "listed_date": financial_sum_result[11].string,
                         "initial_listed_price": financial_sum_result[13].string}

    business_sum = (rows[8].findChildren('td'))
    business_sum_result = business_sum[0].find_all(text=True)
    #print(business_sum_result[2])
    company_desc = business_sum_result[2].string
    b_license = business_sum_result[12].string
    e_license =business_sum_result[11].string
    business_registration ={"business_license": b_license, "established_license": e_license}
    audit_name = str(business_sum_result[5].string)
    audit_address = business_sum_result[6].split(':')
    p_number = business_sum_result[7]
    auditing_company = {"company_name": audit_name.strip('\t,\n '), "company_address": audit_address, 
                        "phone_number": p_number}

    company_profile = {"company_name": company_name,"uid": url,"ticker_symbol":ticker_symbol, "company_description": company_desc.strip('\t,\n '),
                       "country": "Vietnam","company_set_address":company_address, "company_phone_number" : company_phone_num,
                       "business":company_industry, "company_website": company_website.strip('\t,\n '), "company_email":company_email.strip('\t,\n '),
                       "financial_summary": financial_summary, "business_registration": business_registration,
                       "auditing_company": auditing_company}
    return(company_profile)

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
    for cell in cells:
         for a in cell.find_all('a', href=True):
             url = (a['href'])
             
             try:
                 print(url)
                 lis.append(company_profile(url))
             except:
                 print("error: "+ str(url))
                 pass
print(lis)

js = json.dumps(lis)
fp = open('company_profiles.json', 'a')
fp.write(js)
fp.close()