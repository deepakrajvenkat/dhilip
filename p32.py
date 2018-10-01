n,k=map(int,input().split())
l=input().split()
flag=0
for i in range(n):
	if(int(l[i])==k):
		flag=1
		break
if(flag==1):
	print("yes")
else:
	print("no")
