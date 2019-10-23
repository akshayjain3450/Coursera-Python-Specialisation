import re

filename = input("Enter the file name: ")
fd = open(filename)
sum_total = 0

for line in fd:
	line = line.rstrip()
	temp = re.findall('[0-9]+',line)
	for num in temp:
		num = int(num)
		sum_total = sum_total + num
print(sum_total)