n=input()
m=input().split(" ")
m.sort()
o=len(m)
l=[]
for i in range (o):
	flag=0
	for j in range (o):
		if m[i]==m[j] and i!=j:
			flag+=1
	if flag==0:
		print(m[i])
			
