count = 0
fname = raw_input("Enter the file name: ")
try:
    fin = open(fname)
except:
    print('Filename not found')

for line in fin:
    words=line.split()
    if len(words) < 1 or words[0] != 'From': continue
    count = count + 1
    if len(words) < 2: continue
    print words[1]
print 'There were %d lines in the file with From as the first word' % count



