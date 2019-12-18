#!/usr/bin/env python3

import urllib.request
import urllib.error

url = 'http://data.pr4e.org/romeo-full.txt'

try:
    raw_web = urllib.request.urlopen(url).read()
    webpage = raw_web.decode('utf-8')

    print(webpage[:3001])

except urllib.error.URLError:
    print(f'Failed to connect to {url}')
