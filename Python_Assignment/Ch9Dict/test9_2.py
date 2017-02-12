emaildict = dict()
handle = open('mbox-short.txt')
for line in handle:
    words = line.split()
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    emaildict[words[1]] = emaildict.get(words[1],0) + 1
print emaildict