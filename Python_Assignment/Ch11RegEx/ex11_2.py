import re

fin = open('mbox.txt')
count = 0.0
sumnum = 0.0
l = list()
for line in fin:
    num = re.findall('\S*New Revision: ([0-9]*)',line)
    if len(num) > 0 :
        x = float(num[0])
        sumnum = sumnum + x
        count += 1
        l.append(num)
average = sumnum / count
print l
print average