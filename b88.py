n,m=map(int,input().split())
if(n==1 and m==1):
	print(n)
else:
	if(n>m):
		maximum=n
	else:
		maximum=m
	for i in range(1,maximum):
		if(n%i==0 and m%i==0):
			hcf=i
	lcm=(n*m)//hcf
	print(lcm)
