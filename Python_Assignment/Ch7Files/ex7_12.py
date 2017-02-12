fname = raw_input(" Enter the file name : ")
count = 0
total = 0
try:
    fread = open(fname)
except:
    print "File name not found"
    exit()
for line in fread:
    if line.find('X-DSPAM-Confidence:') == -1:
        continue
    pos = line.find(':')
    spamconf = float(line[pos+1:])
    total = total + spamconf
    count = count + 1
    spam_avg = total/count
print(spam_avg)
