# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

position = int(input("Enter the position: "))
# Retrieve all of the anchor tags
count = int(input("Enter the count: "))

for i in range(0,count):
	tags = soup('a')
	temp = position
	for tag in tags:
		if temp > 0:
			url = tag.get('href', None)
			temp = temp - 1
		else:
			print(url)
			break
	html_update =urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html_update, 'html.parser')
name = url.split("/")
name = name[3].split(".")
name = name[0].split("_")
print(name[2])