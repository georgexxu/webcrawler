import argparse
from csv import DictWriter
import json
import sys

from bs4 import BeautifulSoup
import urllib.request as request
import instagram_private_api, instagram_web_api


def getHTML(url):
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req = request.Request(url, headers=headers)
    return request.urlopen(req).read()


class ins_api:
    def __init__(self):
        self.topsearchUrl = "https://www.instagram.com/web/search/topsearch/?context=blended&query="
        self.locationExploreUrl = "https://www.instagram.com/explore/locations/"
        user_name = 'jerry_jiarui_xu'
        password = 'xvjiarui'
        self.app_api = instagram_private_api.Client(user_name, password)
        self.web_api = instagram_web_api.Client()
        
    def to_json(self, url):
        return json.loads(getHTML(url))
    def top_search(self, query):
        return self.to_json(self.topsearchUrl+query)
    def get_location_id(self, search_json):
        return search_json['places'][0]['place']['location']['pk']
    def location_search(self, location):
        return self.web_api.location_feed(location_id=location, count=100)
    def total_like(self, location_json):
        ret = 0
        for p in location_json['location']['media']['nodes']:
            ret += p['likes']['count']
        return ret
        
    # get the like of a query
    def get_like_num(self, query):
        return self.total_like(self.location_search(self.get_location_id(self.top_search(query))))