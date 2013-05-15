#Sahil Shah's Reddit Scraper
#5/12/13

import requests
from bs4 import BeautifulSoup, NavigableString

def get_item(r):
    data = r.json()

    #print data["data"]["children"][0]["data"]["url"]

    for i, v in enumerate(data["data"]["children"]):
        print v["data"]["url"]

def get_request (url):
    r = requests.get(url)
    get_item(r)

def get_url():
    url = 'http://reddit.com/r/villageporn.json'
    
    get_request(url)

get_url()
