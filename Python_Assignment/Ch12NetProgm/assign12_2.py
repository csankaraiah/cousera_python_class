import urllib
from bs4 import BeautifulSoup

urlin = raw_input("Enter URL: ")
count_raw = raw_input("Enter count: ")
position_raw = raw_input("Enter position: ")

count = int(count_raw)
position = int(position_raw)

# urlin = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'
countv = 0

while countv <= count :
    print urlin
    fhand = urllib.urlopen(urlin)
    soup = BeautifulSoup(fhand, "lxml")
    tags = soup('a')
    positionv = 0
    for tag in tags:
        link = tag.get('href',None)
        positionv = positionv + 1
        if positionv == position :
            urlin = link
    countv = countv + 1
