fin = open('mbox-short.txt')
for line in fin :
    words = line.split()
    if len(words) < 3 or words[0] != 'From' : continue
    print words[2]
