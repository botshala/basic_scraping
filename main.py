#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import os
import logging
import re
import json

def scrape_generic(url='http://www.iemoji.com/meanings-gallery/people'):
    arr =[]
    soup = BeautifulSoup( urllib2.urlopen(url).read() )
    for i in soup.find_all('div',{'class' : 'thumbnail'}):
        try:
            a = i.find('a')
            text =  a.get_text()
            link = a.get('href')
            link = 'http://www.iemoji.com/'+link
            emoji = scrape_link(link)
            if not emoji:
                print 'no emoji found'
                continue
            print emoji,text
            arr.append([emoji,text])
        except:
            print 'some error skipping'
            continue

    print len(arr)
    return arr

def scrape_link(url='http://www.iemoji.com/view/emoji/1/people/smiling-face-with-open-mouth-and-smiling-eyes'):
    soup = BeautifulSoup( urllib2.urlopen(url).read() )
    for i in soup.find_all('input',{'id' : 'code'}):
        try:
            return i.get('value')
        except:
            return None

def main():
    tags = 'people;places;nature;objects;symbols;new;skin-tones'.split(';')
    master_arr = []
    for tag in tags:
        master_arr = master_arr + scrape_generic(url='http://www.iemoji.com/meanings-gallery/'+tag)
    f = open('output.json', 'w')
    f.write(json.dumps(master_arr))


def render():
    f = open('output.json','r')
    a = json.loads(f.read())
    arr =[]
    for i in a:
        arr.append([i[0].decode('utf-8','ignore'),i[1]])
    
    g = open('b_output.json','w')
    g.write(json.dumps(arr))

if __name__ == '__main__':
    #render()
    #scrape_link()
    main()
    #scrape_generic()

    

