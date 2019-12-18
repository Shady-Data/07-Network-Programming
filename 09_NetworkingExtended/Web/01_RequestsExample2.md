## Making a simple request
 Let us create our first request for getting a web page, which is very simple. The process includes importing the requests module, and then getting the web page with the get method. Let us look into an example:
```
>>> import requests
>>> r =  requests.get('http://google.com')
```
Simple We are done.

In the preceding example, we get the google webpage, using requests.get and saving it in the variable r, which turns out to be the response object. The response object r contains a lot of information about the response, such as header information, content, type of encoding, status code, URL information and many more sophisticated details.

In the same way, we can use all the HTTP request methods like GET, POST, PUT, DELETE, HEAD with requests.

Now let us learn how to pass the parameters in URLs. We can add the parameters to a request using using the params keyword.

The following is the syntax used for passing parameters:
```
parameters = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('url', params=parameters)
```
For getting a clear picture on this, let us get a GitHub user details by logging into GitHub, using requests as shown in the following code:
```
>>> r = requests.get('https://api.github.com/user', auth=('myemailid.mail.com', 'password'))
>>> r.status_code
200
>>> r.url
u'https://api.github.com/user'
>>> r.request
<PreparedRequest [GET]>
```
We have used the auth tuple which enables Basic/Digest/Custom Authentication to login to GitHub and get the user details. The r.status_code result indicates that we have successfully got the user details, and also that we have accessed the URL, and the type of request.
