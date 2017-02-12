import xml.etree.ElementTree as ET
import urllib

urlin = raw_input("Enter location: ")

data = urllib.urlopen(urlin, "lxml").read()
print 'Retrieving',  urlin

count = 0
sum = 0

xmlsample = ET.fromstring(data)
lst = xmlsample.findall('comments/comment/count')

for item in lst:
    num = int(item.text)
    count = count + 1
    sum = sum + num
print count
print sum