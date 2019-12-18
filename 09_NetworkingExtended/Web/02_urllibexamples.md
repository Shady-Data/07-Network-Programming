# urllib examples

## urllib.request

This module helps to define functions and classes to open URLs (mostly HTTP). 
One of the most simple ways to open such URLs is :
```
urllib.request.urlopen(url)
```
We can see this in an example:
```python
import urllib.request 
request_url = urllib.request.urlopen('https://www.google.com/') 
print(request_url.read())
```
output 
Is going to be raw html information. 

 ## URLLIB.PARSE: SPLIT URLS INTO COMPONENTS
The urllib.parse module provides functions for manipulating URLs and their component parts, to either break them down or build them up.
### Parsing
The return value from the urlparse() function is a ParseResult object that acts like a tuple with six elements.

### urllib_parse_urlparse.py


```python

       from urllib.parse import urlparse



       url = 'http://netloc/path;param?query=arg#frag'

       parsed = urlparse(url)

       print(parsed)
```
The parts of the URL available through the tuple interface are the scheme, network location, path, path segment parameters (separated from the path by a semicolon), query, and fragment.

```python


       $ python3 urllib_parse_urlparse.py



       ParseResult(scheme='http', netloc='netloc', path='/path',

       params='param', query='query=arg', fragment='frag')
```

Although the return value acts like a tuple, it is really based on a namedtuple, a subclass of tuple that supports accessing the parts of the URL via named attributes as well as indexes. In addition to being easier to use for the programmer, 
the attribute API offers access to several values not available in the tuple API.

Documentation maybe found at https://docs.python.org/3/library/urllib.html

