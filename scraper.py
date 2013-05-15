#Sahil Shah's Reddit Scraper
#5/12/13

import requests
from bs4 import BeautifulSoup, NavigableString
import webbrowser

#get specified item
#in this case, vilalgeporn url for the front page of the subreddit
def get_item(r):
    data = r.json()

    image = data["data"]["children"][0]["data"]["url"]
	
	#opens image url in defaulr web browser
    webbrowser.open(image,new=1,autoraise=True)

    for i, v in enumerate(data["data"]["children"]):
        print v["data"]["url"]

#gets the request object from passed in url
def get_request (url):
    r = requests.get(url)
    get_item(r)

#gets url from user and passes to get_request funtion
#normally would have input of some sort but in this case i defaulted to the below link
def get_url():
    url = 'http://reddit.com/r/villageporn.json'
    
    get_request(url)

get_url()
