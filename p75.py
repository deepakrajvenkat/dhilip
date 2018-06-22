from itertools import combinations
n=input()
input1=input()

list1=input1.split(" ")
list1.sort()
comb=combinations(list1,2)
list2=[]
for i in list(comb):
	list2.append(list(i))
print(list2)
sum=0
for i in range(len(list2)):
	if list2[i][0]<list2[i][1]:
		sum=sum+1
print(sum)	
