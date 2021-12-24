from django.conf import Settings, settings
from selectorlib import Extractor
import requests 
import json 
from time import sleep
import os
import pyuser_agent

e = Extractor.from_yaml_file('modules/webscraper/selectors.yml')

def scrape(url):  

    url = "https://www.amazon.de/" + url
   
    headers = {
        'authority': 'www.amazon.de',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'User-Agent': pyuser_agent.UA().random, # Rotate user agent 
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
    }

    r = requests.get(url, headers=headers)

    print(r.text)

    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n"%url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d"%(url,r.status_code))
        return None
    # Pass the HTML of the page and create 
    return e.extract(r.text)
    