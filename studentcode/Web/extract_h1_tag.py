#!/usr/bin/env python3

import urllib.request
import urllib.error
import re
from sys import argv, exit

try:
    url = argv[1]
except (IndexError, ValueError):
    print('Must supply an RFC number as first argument')
    exit(2)
try:
    rfc_raw = urllib.request.urlopen(url).read()
    rfc = rfc_raw.decode('utf-8')
    # print(rfc_raw)
    # print(rfc)
    h1tags = re.findall(r'(<h1.*>$)', rfc, re.M)

    if h1tags:
        for tag in h1tags:
            print(tag)
    else:
        print('no HTML h1 tags found')

except urllib.error.URLError as e:
    print('Error:', e.reason)
