'''

The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the
JSON data and compute the sum of the numbers in the file.

'''

import json

import urllib.request, urllib.parse, urllib.error

url = input('Enter url: ')

uh = urllib.request.urlopen(url)

data = uh.read()

info = json.loads(data)['comments']

counts = 0

for user in info:
  counts += user['count']

print(counts)
