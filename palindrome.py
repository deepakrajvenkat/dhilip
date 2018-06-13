n=input()
if n.isdigit():
	n=int(n)
	temp=n
	if n<=10000:
		sum=0
		while(n>0):
			rem=n%10
			sum=((sum*10)+(rem))
			n=n//10
		if (sum==temp):
			print ("yes")
		else:
			print("no")
			
	else:
		print ("enter the no between 1 to 10000")
else:
	print ("Invalid Input")
