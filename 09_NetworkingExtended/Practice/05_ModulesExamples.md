How Modules make it  easier to write scripts and going down levels to see the background work.

Let’s begin with a simple example. Here is a mailing address:
```
207 N. Defiance St
Archbold, OH
```

## Fetching a Longitude and Latitude
```python
#!/usr/bin/env python3
# search1.py 

from pygeocoder import Geocoder

if __name__ == '__main__':
    address = '207 N. Defiance St, Archbold, OH'
    print(Geocoder.geocode(address)[0].coordinates)
```
By running it at the command line, you should see a result like this:
```
$ python3 search1.py
(41.521954, -84.306691)
```
## Fetching a JSON Document from the Google Geocoding API
```python
#!/usr/bin/env python3
#search2.py

import requests

def geocode(address):
    parameters = {'address': address, 'sensor': 'false'}
    base = 'http://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base, params=parameters)
    answer = response.json()
    print(answer['results'][0]['geometry']['location'])

if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
```
Running this Python program returns an answer quite similar to that of the first script.
```
$ python3 search2.py
{'lat': 41.521954, 'lng': -84.306691}
```
## Making a Raw HTTP Connection to Google Maps
```python
#!/usr/bin/env python3
# search3.py

import http.client
import json
from urllib.parse import quote_plus

base = '/maps/api/geocode/json'

def geocode(address):
    path = '{}?address={}&sensor=false'.format(base, quote_plus(address))
    connection = http.client.HTTPConnection('maps.google.com')
    connection.request('GET', path)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    print(reply['results'][0]['geometry']['location'])

if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
```
The result of running the program, however, is much the same as for the programs shown previously.
```
$ python3 search3.py
{'lat': 41.521954, 'lng': -84.306691}
```

