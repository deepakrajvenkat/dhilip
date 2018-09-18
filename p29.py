x,y=map(int,input().split())
count=0
for i in range(x,y):
	for j in range(100):
		a=j*j
		if(a==i):
			count=count+1
		elif(a>i):
			break
print(count)		
