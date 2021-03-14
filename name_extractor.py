'''
The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan
for a tag that is in a particular position relative to the first name in the list, follow that link  and repeat the process
a number of times and report the last name you find.
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Catherine.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last
name that you retrieve.
'''

# 'a' determines how many times will the loop repeat (actually it's second integer of 'range' function)
# def html_parser(url, a):
url = input('Input url: ')
a = int(input('Input desired number of loops: '))

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
print(tags[17].contents)
for x in range(1,a):
    url = tags[17].get('href', None)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print(tags[17].contents)
