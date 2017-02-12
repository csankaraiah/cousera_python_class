import re
regex = raw_input('Enter a regular expression: ')
count = 0
fin = open('mbox.txt')
for line in fin :
    if re.search(regex, line) : count +=1
print 'mbox.txt has %d lines that matched ' % count + regex
