n=input()
if n.isdigit():
	n=int(n)
	sum=1
	while(n>0):
		sum=sum*n
		n-=1
	print (sum)	
else:
	print ("invalid input")
	
