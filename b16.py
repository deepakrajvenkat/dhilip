s=input()
l=s.split(" ")
n=int(l[0])
m=int(l[1])
L=[]
for i in range (n,m):
	flag=0
	if(i==2):
		flag=0
	elif(i==1):
		flag=1
	else:
		
		for x in range(2,i):
			if ((i%x)==0):
				flag=1
				break
	if flag==0:
		L.append(str(i))
print(" ".join(L))
