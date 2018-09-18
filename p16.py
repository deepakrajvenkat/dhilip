n=int(input())
l=input().split()
l2=[]
for i in range(n):
	count=0
	if(l[i] in l2):
		continue
	l2.append(l[i])
	for j in range(n):
		if(l[i]==l[j]):
			count=count+1
	if(count==1):
		print(l[i])
	
