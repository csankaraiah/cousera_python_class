import sys

try:
    if len(sys.argv[1])>0:
        filename = sys.argv[1]
    print filename
except:
    print 'Please enter a argument'

