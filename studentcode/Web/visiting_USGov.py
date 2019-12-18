#!/usr/bin/env python3

import requests

url = 'https://analytics.usa.gov/data/live/realtime.json'

try:
    web_analytics = requests.get(url).json()
    print('Active Visitors on usa.gov:', web_analytics['data'][0]['active_visitors'])

except requests.exceptions.ConnectionError:
    print("Failed to connect to remote server")
