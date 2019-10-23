name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = dict()
for line in handle:
	if line.startswith("From ") == True:
		line = line.rstrip()
		words = line.split()
		dic[words[1]] = dic.get(words[1],0) + 1
longword = None
longcount = None

for key,value in dic.items():
	if longcount is None or value > longcount:
		longword = key
		longcount = value

print(longword,longcount)