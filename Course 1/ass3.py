hrs = input("Enter Hours:")
h = float(hrs)
rate = 10.50
if h <= 40:
	pay = h * rate
	print(pay)
else:
	pay = 40*rate + (h-40)*1.5*rate
	print(pay)