#!/usr/bin/python3

#This script is intended to help with:

#checking the liquidation.com best deals
import selenium

from selenium import webdriver

browser=webdriver.Chrome("/Users/TheKillagrams/Downloads/chromedriver")

browser.get("https://www.liquidation.com/auction/search?query=TQ3xL222Tyj49f2ckN2hKN1akN2h22VV&flag=new")



item = browser.find_element_by_class_name('desc')
itemHref = item.get_property('href')

print (itemHref)

browser.get(itemHref)



#import beautifulsoup4
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
client = uReq(itemHref)
pageHtml = client.read()
shippingClient.close()
pageSoup = soup(pageHtml, 'html.parser')
title = pageSoup.h1
print (title)

