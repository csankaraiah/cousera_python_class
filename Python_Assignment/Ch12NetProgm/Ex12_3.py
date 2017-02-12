import re
import urllib
#from BeautifulSoup import *
from bs4 import BeautifulSoup

#urlin = raw_input('Enter the URL for the page : ')

# website link GET http://www.py4inf.com/code/romeo.txt HTTP/1.0 \n\n

urlin = 'https://jobs.target.com/job/minneapolis/lead-data-engineer-hadoop/1118/1204310?ss=paid'

fhand = urllib.urlopen(urlin)
soup = BeautifulSoup(fhand)

tags = soup('div')
for tag in tags:
    print tag
   # print tag.get('href',None)



'''
count = 0
outlist = list()
for line in fhand:
    if ( len(line) < 1): break
    for ch in line :
        tlist = list(ch)
        for i in range(len(tlist)):
            if count < 10000 :
                count = count + 1
                outlist.append(tlist[i])
print ''.join(outlist)
print 'Number of character printed %d' % count

'''