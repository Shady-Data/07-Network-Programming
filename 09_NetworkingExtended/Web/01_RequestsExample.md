# Downloading web pages
The basic ability to download a web page involves making an HTTP GET request against a URL. This is the basic operation of any web browser. Let's quickly recap the different parts of this operation:
```
Using the HTTP protocol.
Using the GET method, which is the most common HTTP method. We'll see more in the Accessing web APIs recipe.
URL describing the full address of the page, including the server and the path.
```
That request will be processed by the server and a response will be sent back. This response will contain a status code, typically 200 if everything went fine, and a body with the result, which will normally be text with an HTML page.

Most of this is handled automatically by the HTTP client used to perform the request. We'll see in this recipe how to make a simple request to obtain a web page.

HTTP requests and responses can also contain headers. Headers contain extra information, such as the total size of the request, the format of the content, the date of the request, and what browser or server is used. 

## Example utilization

Import the requests module:
```
>>> import requests
```
Make a request to the URL, which will take a second or two:
```
>>> url = 'http://www.columbia.edu/~fdc/sample.html'
>>> response = requests.get(url)
```
Check the returned object status code:
```
>>> response.status_code
200
```
Check the content of the result:
```
>>> response.text
'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">\n<html>\n<head>\n
...
FULL BODY
...
<!-- close the <html> begun above -->\n'
```
Check the ongoing and returned headers:
```
>>> response.request.headers
{'User-Agent': 'python-requests/2.18.4', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
>>> response.headers
{'Date': 'Fri, 25 May 2018 21:51:47 GMT', 'Server': 'Apache', 'Last-Modified': 'Thu, 22 Apr 2004 15:52:25 GMT', 'Accept-Ranges': 'bytes', 'Var
```
# What's going on:
The operation of requests is very simple; perform the operation, GET in this case, over the URL. This returns a result object that can be analyzed. The main elements are the status_code and the body content, which can be presented as text.

The full request can be checked in the request field:
```
>>> response.request
<PreparedRequest [GET]>
>>> response.request.url
'http://www.columbia.edu/~fdc/sample.html'
```
The full request's documentation can be found here: http://docs.python-requests.org/en/master/. 
