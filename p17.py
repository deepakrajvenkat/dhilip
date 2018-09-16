n,m=map(int,input().split())
if(n<m):
	min=n
else:
	min=m
for i in range(1,min+1):
	if(n%i==0 and m%i==0):
		hcf=i
print(n*m//hcf)
