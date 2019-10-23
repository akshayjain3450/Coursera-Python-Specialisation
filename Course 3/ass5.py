import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
from urllib.request import urlopen
api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
stuff = ET.fromstring(html)
lst = stuff.findall('.//comment')
print('User count:', len(lst))
value = 0
total = 0
for items in lst:
    temp = items.find('count').text
    value = int(temp)
    total = total + value
print(total)