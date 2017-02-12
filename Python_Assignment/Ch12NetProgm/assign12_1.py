import urllib
from bs4 import BeautifulSoup

urlin = 'http://python-data.dr-chuck.net/comments_203809.html'

fhand = urllib.urlopen(urlin)
soup = BeautifulSoup(fhand, "lxml")

tags = soup('span')
sum = 0
count = 0
for tag in tags:
    num = int(tag.text)
    count = count +1
    sum = num + sum
print "Count " , count
print "Sum " , sum