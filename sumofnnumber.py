n=input()
if n.isdigit():
	n=int(n)
	if n < 0:
		print ("enter the postive integer")
	else:
		sum=0
		while(n > 0):
			sum+= n
			n-= 1
		print (sum)
else:
	print("invalid input")
