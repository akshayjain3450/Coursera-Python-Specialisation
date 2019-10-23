name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
	if line.startswith("From "):
		line = line.rstrip()
		words = line.split()
		time = words[5].split(":")
		counts[time[0]] = counts.get(time[0],0) + 1

lst = list()
for key,value in counts.items():
	newtup = (key,value)
	lst.append(newtup)

lst = sorted(lst)

for key,value in lst:
	print(key,value)