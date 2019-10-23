largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try:
    	fval = int(num)
    	if largest == None and smallest == None:
    		largest = ival
    		smallest = ival
    	else:
    		if largest < ival:
    			largest = ival
    		if smallest > ival:
    			smallest = ival
    except:
    	print("Invalid Input")
    	continue

print("Maximum", largest)
print("Minimum", smallest)