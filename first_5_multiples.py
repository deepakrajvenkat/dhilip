n=input()
if n.isdigit():
	n=int(n)
	for i in range (1,6):
		val=i*n
		print (val)
else:
	print("invalid input")
