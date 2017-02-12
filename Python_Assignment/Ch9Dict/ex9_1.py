fin = open('romeo.txt')
dwords = dict()
for line in fin:
    words = line.split()
    for i in range(len(words)):
        dwords[words[i]] = ''
print dwords
