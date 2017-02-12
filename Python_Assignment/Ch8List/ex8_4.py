fin = open('romeo.txt')
wordlist = list()
for line in fin:
    words = line.split()
    if len(words) == 0 : continue
    for i in range(len(words)) :
        if words[i] in wordlist : continue
        wordlist.append(words[i])
wordlist.sort()
print wordlist

