low=input()
list1=low.split(" ")
n=int(list1[0])
m=int(list1[1])
list2=[]
for i in range (n,m):
	if ((i%2)!=0):
		list2.append(str(i))
print(" ".join(list2))
