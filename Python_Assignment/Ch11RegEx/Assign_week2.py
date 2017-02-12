import re

fin = open('regex_sum_203804.txt')
count = 0
sumnum = 0
l = list()
for line in fin:
    num = re.findall('([0-9]+)',line)
    if len(num) > 0 :
        for i in range(len(num)):
            x = int(num[i])
            sumnum = sumnum + x
            count += 1
            l.append(num)
print count , sumnum