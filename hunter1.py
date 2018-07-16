n=input()
m=input().split(" ")
m.sort()
o=len(m)
l=[]
flag=0
for i in range (o):
	for j in range (i,o):
		if m[i]==m[j] and i!=j:
			flag+=1
			l.append(m[i])
if (flag>=1):
	str=" ".join(l)
	print(str)
else:
	print("unique")
