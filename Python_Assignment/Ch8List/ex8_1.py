def chop(lin):
    lastindex = len(lin)
    del lin[lastindex-1]
    del lin[0]
    print lin
    return None

def middle(lin2):
    lastind = len(lin2)
    linnew = lin2[1:lastind-1]
    return linnew


lin = [8,9,10,2,3,4]
lin = chop(lin)
print lin

lin2 = [9,8,7,6,5,4]
linenew = middle(lin2)
print lin2
print linenew