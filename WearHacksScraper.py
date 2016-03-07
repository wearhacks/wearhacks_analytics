# -*- coding: utf-8 -*-
"""
Created on Sat Mar 05 13:01:32 2016

@author: John
"""

from lxml import html
import requests
import xlwt


sheets = ["Sheet 1", "Sheet 2", "Sheet 3"]

wb = xlwt.Workbook()


sheet1 = wb.add_sheet('sheet 1')
row = 0
for i in range(44,530):      # Number of pages plus one 
    url = "http://postscapes.com/companies/r/{}".format(i)
    page = requests.get(url)
    tree = html.fromstring(page.content)




    #This will create a list of prices
    companyname = tree.xpath('//span[@itemprop="name"]/text()')
    
    #This will create a list of buyers:
    companysize = tree.xpath('//div[@class="detailscompany"]/text()')
    
    #This will create a list of prices
    contactname = tree.xpath('//*[@id="rt-mainbody"]/div/div/div[2]/div[4]/address/strong/text()')
    contactnumber = tree.xpath('//*[@id="rt-mainbody"]/div/div/div[2]/div[4]/address/text()')
    

    while '\n' in companysize: companysize.remove('\n')
    while ' ' in companysize: companysize.remove(" ")
        
    while '\n' in contactnumber: contactnumber.remove('\n')
    while ' ' in contactnumber: contactnumber.remove(" ")
    while '\n\n' in contactnumber: contactnumber.remove("\n\n") 
    
    while '\n' in contactname: contactname.remove('\n')
    while ' ' in contactname: contactname.remove(" ")
    while '\n\n' in contactname: contactname.remove("\n\n") 
    

    sheet1.write(row,0, companyname)
    sheet1.write(row,1, companysize)
    sheet1.write(row,2, contactnumber)
    sheet1.write(row,3, contactname)
    row += 1
wb.save('output7.xls')
