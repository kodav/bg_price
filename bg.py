# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib2 import urlopen
import datetime
import time
import sys

if (len(sys.argv) != 2):
    print ('set args')
    sys.exit()

url = sys.argv[1]
now = datetime.datetime.now()

if (url == ''):
    print ('url is empty')
    sys.exit()

html_doc = urlopen(url).read()
soup = BeautifulSoup(html_doc, "html.parser")

pe = soup.find('div', 'pe')
if (pe):
    price = pe.find("b", {"class": "r"})
    if (price):
        ptext = price.text
    else:
        ptext = '0'
else:
    ptext = 'ERROR'

print(time.strftime("%Y-%m-%d %H:%M:%S") + ": " + ptext + "\n")
