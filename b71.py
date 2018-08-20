n=input()
l=[]
for i in range (len(n)):
	l.append(n[-1-i])
rev="".join(l)
if(n==rev):
	print("yes")
else:
	print("no")
