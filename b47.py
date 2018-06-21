n=int(input())
m=input()
l=m.split()
length=len(l)
if length==n:
	l.sort()
	print (l[0],l[-1])
else:
	print ("invalid input")
