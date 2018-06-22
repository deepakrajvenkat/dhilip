input1=input()
r=input1.split(" ")
n=int(r[0])
m=int(r[1])
x=input()
list1=x.split(" ")
length_list=len(list1)
if (length_list==n):
	list2=[]
	for i in range(n-1):
		list2.append(int(list1[i+1])-int(list1[i]))
	p=1
	q=-1
	flag=0
	for i in range(n-1):
		if list2[i]==p or list2[i]==q:
			flag=flag+1
	if(flag==(n-1)):
		for j in range(n):
			if int(list1[j])==m:
				k=list1.index(str(m))
				print(k+1)
				break
else:
	print("invalid input")
