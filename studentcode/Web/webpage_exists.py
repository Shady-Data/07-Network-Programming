#!/usr/bin/env python3

import requests
from sys import argv, exit

try:
    url = argv[1]
except IndexError:
    print('Cannot continue without a url as the first argument')
    exit(2)

try:
    web_status = requests.get(url).status_code

    if web_status in range(200, 300):
        print(f'{url}\n\tExists\tCode: {web_status}')
    elif web_status in range(300, 400):
        print(f'{url}\n\tRedirects\tCode: {web_status}')
    else:
        print(f'{url}\n\tDoes not exist/Unavailable\tCode: {web_status}')

except requests.exceptions.ConnectionError:
    print(f'{url}\n\tDoes not exist/Unavailable')
