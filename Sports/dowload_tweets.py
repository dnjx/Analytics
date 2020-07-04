# resource url: https://api.twitter.com/1.1/search/tweets.json

import urllib.request, urllib.parse, urllib.error
from twurl import augment
import ssl

parameters = dict()
parameters["q"] = '<insert search query>'
parameters["lang"]  = 'en'
parameters["result_type"] = 'recent'
parameters["count"] = '100'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = augment('https://api.twitter.com/1.1/search/tweets.json', parameters)

connection = urllib.request.urlopen(url, context=ctx)

data = connection.read()
print(data)
headers = dict[connection.getheaders()]
print(headers)
