n=int(input())
l=[]
while(n>0):
	digit=n%10
	n=n//10
	l.append(str(digit))	
s=" ".join(l)
print(s[::-1])
