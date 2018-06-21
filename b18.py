s=input()
l=s.split(" ")
n=int(l[0])
m=int(l[1])
list2=[]
for i in range (n,m):
	sum=0
	temp=i
	while(i>0):
		rem=i%10
		c=rem*rem*rem
		sum+=c
		i=i//10
	if sum==temp:
		list2.append(str(temp))
print (" ".join(list2))		
