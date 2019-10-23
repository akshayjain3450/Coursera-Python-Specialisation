# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
value = 0
start = len("X-DSPAM-Confidence:")
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
    	continue
    count = count + 1
    valstr = line[start+1:]
    valstr = valstr.rstrip()
    value = value + float(valstr)
average = value / 27
print("Average spam confidence:",average)
