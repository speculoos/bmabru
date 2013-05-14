"""
html parser
"""

from HTMLParser import HTMLParser
import urllib
import sys
import json

class TextNode(object):
    def __init__(self, txt = '', parent = None):
        self.parent = parent
        self.text = txt
        self.children = []
        
    def append(self, txt):
        c = TextNode(txt, self)
        self.children.append(c)
        return c
        
    def root(self):
        c = self
        while c.parent is not None:
            c = self.parent
        return c
        
    def dump(self):
        r = self.root
        txt = []
        self.r_dump(txt)
        return u' '.join(txt)
        
    def r_dump(self, txt):
        txt.append(self.text)
        for c in self.children:
            c.r_dump(txt)

        
class Parser(HTMLParser):
    STATE_NONE = 0
    STATE_META = 1
    STATE_CONTENT = 2
    STATE_IMAGE = 3
    
    def __init__(self, url=None):
        HTMLParser.__init__(self)
        self.meta = {}
        self.contents = ['']
        self.images = []
        
        self._state = [self.STATE_NONE]
        self._states = { 
            'head': self.STATE_META,
            'img': self.STATE_IMAGE,
            #'body': self.STATE_CONTENT,
            'header': self.STATE_CONTENT,
            'p': self.STATE_CONTENT,
            'div': self.STATE_CONTENT,
            'span': self.STATE_CONTENT,
            'a': self.STATE_CONTENT,
            'h1': self.STATE_CONTENT,
            'h2': self.STATE_CONTENT,
            'h3': self.STATE_CONTENT,
            'h4': self.STATE_CONTENT,
            }
            
        self.content_depth = 0
        self.textnode = TextNode()
        self.current_tag = None
        
        if url:
            try:
                self.start_parser(url)
            except Exception:
                pass
        
    def start_parser(self, url):
        connection = urllib.urlopen(url)
        encoding = connection.headers.getparam('charset')
        page = connection.read().decode(encoding)
        self.feed(page)

    def handle_starttag(self, tag, attrs):
        st = self.push_state(tag)
        self.current_tag = tag
        
        if st == self.STATE_IMAGE:
            kattrs = {}
            for k,a in attrs:
                kattrs[k] = a
            self.images.append(kattrs)
        elif st == self.STATE_CONTENT:
            self.content_depth += 1
            
    def handle_endtag(self, tag):
        if tag != self.current_tag:
            print 'Closing %s when %s is still open'%(tag, self.current_tag)
        st = self.pop_state(tag)
        if st == self.STATE_CONTENT:
            self.content_depth -= 1
            if self.content_depth == 0:
                self.contents.append(self.textnode.dump())
                self.textnode = TextNode()
        
    def handle_data(self, data):
        #print('%s %s %s'%(self.state(), self.current_tag, data))
        if self.state() == self.STATE_CONTENT:
            self.textnode.append(data)
        elif self.state(True) == self.STATE_META:
            if not self.current_tag in self.meta:
                self.meta[self.current_tag] = data
            else :
                self.meta[self.current_tag] += data
        
    def to_json(self):
        ret = {
            'meta':self.meta,
            'content':self.contents,
            'images':self.images
        }
        return json.dumps(ret, indent=2);
        
    def state(self, deep = False):
        try:
            if deep == False:
                return self._state[-1]
            else:
                for s in self._state[::-1]:
                    if s is not self.STATE_NONE:
                        return s
        except Exception as e:
            print '[WARNING] %s'%e

    def push_state(self, tag):
        st = self.state()
        if tag in self._states:
            st = self._states[tag]
        self._state.append(st)
        return st
            
    def pop_state(self, tag):
        try:
            return self._state.pop()
        except Exception as e:
            print '[WARNING] %s'%e
            
            

            