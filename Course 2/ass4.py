fname = input("Enter file name: ")
fh = open(fname)
lst = list()
temp = list()
for line in fh:
	line = line.rstrip()
	temp = line.split()
	for element in temp:
		if element in lst:
			continue
		lst.append(element)
lst.sort()
print(lst)