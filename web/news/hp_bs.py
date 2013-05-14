"""
html parser
"""

from bs4 import BeautifulSoup as BS
import urllib
import sys
import json


class Parser(object):
    def __init__(self, url=None):
        self.meta = {}
        self.contents = []
        self.images = []
        
        if url:
            try:
                self.start_parser(url)
            except Exception:
                pass
        
    def start_parser(self, url):
        connection = urllib.urlopen(url)
        self.soup = BS(connection)
        self.get_meta()
        self.get_images()
        self.get_content()
        
    def get_meta(self):
        try:
            self.meta['title'] = self.soup.title.string
        except Exception:
            self.meta['title'] = ''
        for m in self.soup.head.find_all('meta'):
            try:
                self.meta[m.attrs['name']] = m.attrs['content']
            except Exception:
                pass
            
    def get_images(self):
        for i in self.soup.find_all('img'):
            self.images.append(i.attrs)
            
    def get_content(self):
        for p in self.soup.body.find_all('p'):
            if p.string:
                self.contents.append(p.string)
            

    def to_json(self):
        ret = {
            'meta':self.meta,
            'content':self.contents,
            'images':self.images
        }
        return json.dumps(ret, indent=2);
        
            
            

            