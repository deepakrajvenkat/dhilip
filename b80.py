n=input()
l=[]
for i in range(len(n)):
	if(int(n[i])%2==1):
		l.append(n[i])
s=" ".join(l)
print(s)
