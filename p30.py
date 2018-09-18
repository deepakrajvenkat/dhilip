s1,s2,n=map(str,input().split())
l1=list(s1)
l2=list(s2)
n=int(n)
count=0
for i in range(len(l1)):
	if(l1[i]!=l2[i]):
		count=count+1
if(count==n):
	print("yes")
else:
	print("no")
