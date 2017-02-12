fin = open('mbox-short.txt')
daydict = dict()
for line in fin :
    if not line.startswith("From"): continue
    words = line.split()
    if len(words) < 3: continue
    daydict [words[2]] = daydict.get(words[2],0) + 1
print daydict
