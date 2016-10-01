#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import os
import logging
import re
import json
import requests
import hashlib
import string
import random

def main():
    url='https://paytm.com/care'
    arr =[]
    soup = BeautifulSoup( urllib2.urlopen(url).read() )
    for i in soup.find_all('div',{'class' : 'listing'}):
        try:
            print i.get_text()
        except:
            print 'some error skipping'
            continue


if __name__ == '__main__':
	main()