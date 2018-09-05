x,y=map(int,input().split())
for i in range(1,x):
	if(x%i==0 and y%i==0):
		hcf=i
print(hcf)
