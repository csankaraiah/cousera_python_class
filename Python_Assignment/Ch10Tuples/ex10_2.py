fin = open('mbox-short.txt')
hrCnt = dict()
for line in fin:
    words = line.split()
    if len(words) < 1 : continue
    if words[0] != 'From' : continue
    time = words[5]
    hr = time[0:2]
    if hr not in hrCnt :
        hrCnt[hr] = 1
    else:
        hrCnt[hr] += 1
l = list()
for key, val in hrCnt.items():
    l.append((key,val))
    l.sort()
for key,val in l[:]:
    print key, val
