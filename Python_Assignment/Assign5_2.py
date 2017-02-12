largest = None
smallest = None
while True:
    try:
        num = raw_input("Enter a number: ")
        if  num == "done" : break
        num_int = int(num)
        if (largest == None or num_int > largest) : largest = num_int
        if (smallest == None or num_int < smallest) : smallest = num_int
    except:
        print ("Invalid input")
print ("Maximum is "), largest
print ("Minimum is "), smallest