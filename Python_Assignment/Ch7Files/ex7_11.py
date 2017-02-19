fname = raw_input(" Enter the file name : ")
try:
    fread = open(fname)
except:
    print "File name not found"
    exit()
for line in fread:
    line_up = line.upper()
    print(line_up)

