import requests
from requests import session
import bs4
from bs4 import BeautifulSoup
import time

class Bot(object):
    def find(self, link, keywords):
        self.start_time = time.time()
        self.link = link
        self.keywords = keywords
        session = requests.session()
        sitemap = session.get(self.link)
        data = sitemap.text
        soup = BeautifulSoup(data, "lxml")
        items = soup.find_all("url")
        total_items = len(items)
        for i in range(len(items)):
            for item in items[i]:
                name = items[i]["image:image"]
                if self.keywords in name:
                    url = items[i]["loc"]
                    break
                else:
                    pass
                    
        self.end_time = time.time()
        self.time_taken = self.end_time - self.start_time
        print "Searched {} products in {} seconds".format(total_items, self.time_taken)

Scrape = Bot()
Scrape.find("", "")
#1st blank is for the products sitemap URL
#2nd blank is for Keywords
'''If you can figure out the error in line 20, this will work for you, I used cncpts product sitemap
hmu on twitter if you get it'''
