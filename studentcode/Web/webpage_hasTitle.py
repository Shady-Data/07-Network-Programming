#!/usr/bin/env python3

import urllib.request
import urllib.error
from bs4 import BeautifulSoup
from sys import argv, exit

try:
    url = argv[1]
except IndexError:
    print('Must supply a URL as the first argument')
    exit(2)
try:
    web_raw = urllib.request.urlopen(url).read()
    web = BeautifulSoup(web_raw.decode('utf-8'), 'html.parser')

    if web.title:
        print(f'Has title {web.title}')
    else:
        print('Title aws not found')

except urllib.error.URLError as e:
    print('Error:', e.reason)

