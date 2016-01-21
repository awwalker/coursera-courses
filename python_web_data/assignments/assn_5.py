#! /usr/bin/env python2.7
import urllib
from bs4 import BeautifulSoup
import ssl

url = raw_input("Enter - ")
position = int(input("Enter Position: "))
count = int(input("Enter Count: "))

scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

uh = urllib.urlopen(url, context = scontext)
print uh
data = uh.read()
soup = BeautifulSoup(data, "html.parser")

#get all anchor tags
anchors = soup('a')
#repeat count times
for i in range(count):
    #check for position -1
    print "Retrieving:", anchors[position - 1].get('href')
    uh = urllib.urlopen(anchors[position - 1].get('href'), context = scontext)
    #reset variables
    data = uh.read()
    soup = BeautifulSoup(data, "html.parser")
    anchors = soup('a')
