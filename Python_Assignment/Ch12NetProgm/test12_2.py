line = 'this is to see if i can count the character'
print len(line)
count = 0
tlist = list(line)
outlist = list()
for i in range(len(tlist)):
    if count < 5 :
        count = count + i
        outlist.append(tlist[i])
print ''.join(outlist)


