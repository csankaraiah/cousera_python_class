numlist = list()
while True:
    in_raw = raw_input("Enter a number or enter done if you have done entering the number: ")
    if in_raw == 'done': break
    try:
        in_num = float(in_raw)
        numlist.append(in_num)
    except:
        print 'Not a valid entry'
print max(numlist)
print min(numlist)