n=input()
m=input().split(" ")
l=[]
flag=0
for i in range (len(m)):
	if (int(m[i])==i):
		flag+=1
		l.append(m[i])
if flag>=1:
	str=" ".join(l)
	print (str)
else:
	print("-1")
