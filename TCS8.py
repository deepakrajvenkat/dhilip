n=input()
m=input()
for i in range(n,m):
	flag=0
	for j in range(2,i):
		if(i%j==0):
			flag=flag+1
	if(flag==0):
		print(i)
