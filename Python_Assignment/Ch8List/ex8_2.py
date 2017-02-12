fin = open('mbox-short.txt')
for line in fin :
    if not line.startswith("From"): continue
    words = line.split()
    if len(words) < 3: continue
    print words[2]


