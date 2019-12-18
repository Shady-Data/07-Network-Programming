#!/usr/bin/env python3

import urllib.request
import urllib.error
from bs4 import BeautifulSoup
from sys import argv, exit

try:
    url = argv[1]
except (IndexError, ValueError):
    print('Must supply an RFC number as first argument')
    exit(2)
try:
    web_raw = urllib.request.urlopen(url).read()
    web = BeautifulSoup(web_raw.decode('utf-8'), 'html.parser')

    headers = ['h1', 'h2', 'h3']
    htags = []
    
    for tag in headers:
        htags.append(web.find_all(tag))

    for num, tag in enumerate(htags, 1):
        if tag:
            print('\tHTML h' + str(num) + ' tags')
            for t in tag:
                print(t)
        else:
            print('\tNo HTML h' + str(num) + ' tags found.')

except urllib.error.URLError as e:
    print('Error:', e.reason)
