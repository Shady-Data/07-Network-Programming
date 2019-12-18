## Introduction to requests
Requests allow you to send requests to an HTTP server and get responses and messages sent by the server. They're available as the Requests package on PyPI. This can either be installed through pip or be downloaded from http://docs.python-requests.org, which hosts the documentation. You can install the requests library on your system in an easy way with the pip command:
```
pip install requests
```
The requests library automates and simplifies many of the tasks that we've been looking at. The quickest way of illustrating this is by trying some examples. The commands for retrieving a URL with Requests are similar to retrieving a URL with the urllib package.

The request.get() function sends a request using the get method with the following syntax:
```
requests.get ('<URL>', params = <object type dict>)
>>> import requests
>>> response = requests.get('http://www.github.com')
```
The requests.get() method returns a response object, where you will find all the information corresponding to the response of our request. These are the main properties of the response object:
```
response.status_code: This is the HTTP code returned by the server
response.content: Here, we will find the content of the server response
response.json(): If the answer is JSON, this method serializes the string and returns a dictionary structure with the corresponding JSON structure
```
We can look at the properties of the response object:
```
>>> response.status_code
200
>>> response.reason
'OK'
>>> response.url
'http://www.github.com/'
>>> response.headers['content-type']
'text/html; charset=utf-8'
```
We can also access the headers properties through the response object:
```
>>> response.request.headers
{'User-Agent': 'python-requests/2.19.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
```
Notice that Requests is automatically handling compression for us. It's including gzip and deflate in an Accept-Encoding header. If we look at the content-encoding response, then we will see that the response was in fact gzip compressed, and Requests transparently decompressed it for us:
```
>>> response.headers['content-encoding']
'gzip'
```
We can look at the response content in many more ways. To get the same bytes object as we got from an HTTPResponse object, perform the following:
```
>>> response.text
'\n\n\n\n\n\n<!DOCTYPE html>\n<html lang="en">\n  <head>\n <meta charset="utf-8">\n <link rel="dns-prefetch"  href="https://avatars2.githubusercontent.com">\n

Checking HTTP headers
The response.headers statement provides the headers of the web server response. Basically, the response is an object dictionary, and with the items() method, we can iterate with the key-value format for access to the header's response.

You can find the following code in the get_headers.py file:
```python
#!/usr/bin/env python3

import requests
response = requests.get('http://github.com')
try:
    for key,value in response.headers.items():
        print('%s: %s' % (key, value))
except Exception as error:
    print('%s' % (error))
```
In this screenshot, we can see the script execution for the github.com domain:

![image](https://user-images.githubusercontent.com/47218880/71008516-5a52de00-20ae-11ea-83cc-12dc0b462c13.png)

We can also find browser add-ons or plugins that can help us in collecting information on the headers that are sent in the requests.
