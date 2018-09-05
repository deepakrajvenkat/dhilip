n=input()
l=list(n)
m=len(l)
for i in range(m):
	if(l[i].isnumeric()):
		print (l[i], end='')
