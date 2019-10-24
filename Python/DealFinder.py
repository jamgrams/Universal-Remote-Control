#!/usr/bin/python

#This script is intended to help with:

#checking the liquidation.com best deals



from selenium import webdriver

browser=webdriver.Chrome("/Users/TheKillagrams/Downloads/chromedriver")

browser.get("https://www.liquidation.com/auction/search?query=TQ3xL222Tyj49f2ckN2hKN1akN2h22VV&flag=new")
#grabs first item AFAIK
browser.find_element_by_class_name('list-group-image')

firstItem = browser.find_element_by_class_name('list-group-image')


firstItem = browser.find_element_by_class_name('desc')

firstItemURL = firstItem.get_property('href')

browser.get(firstItemURL)

quantity = browser.find_element_by_class_name('col-xs-8') 

#Get manifest and URL and open

manifest = browser.find_element_by_class_name('track-ga view_manifest')

shipping = browser.find_element_by_class_name('track-ga ship-quote')

shippingURL = shipping.get_property('href')

manifestURL = manifest.get_property('href')

URL = (manifestURL)
browser.get(manifestURL)

#import beautifulsoup4

import bs4

from bs4 import beautifulsoup as soup

from urllib.request import urlopen as uReq

client = uReq(URL)

pageHtml = client.read()

shippingClient.close()


pageSoup = soup(pageHtml, 'html.parser')

title = pageSoup.h1

print title








#use beautifulsoup to parse this into a csv in google

#once in google I can fuck with it more?





#Sort by types and go for a under 100 bucks

# 	and about 2.1- 3k in value and pull the top

#	check shipping :

# go to get quote link

# enter 94303

# add to email/message

# 	X number and send a text message or email 

# Attach CSV and use for future listing if purchased

#
#
#
#
