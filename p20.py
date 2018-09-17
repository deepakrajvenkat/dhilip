n=input()
l=list(n)
l2=[]
for i in range(len(l)):
	s=ord(l[i])
	s=s+3
	c=chr(s)
	l2.append(c)
print("".join(l2))
