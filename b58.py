x,y=map(int,input().split())
s=input()
count=0
l=list(s)
for i in range(len(l)):
	if(l[i]==str(y)):
		count+=1
if(count==0):
	print("no")
else:
	print("yes")
