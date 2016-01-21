#! /usr/bin/env python2.7
import urllib
from bs4 import BeautifulSoup

url = raw_input("Enter - ")
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

# get all span tags
tags = soup('span')

# accumulator
sum_tags = 0
for tag in tags:
    sum_tags += int(tag.string)

print "Sum", sum_tags
print "Count", len(tags)
