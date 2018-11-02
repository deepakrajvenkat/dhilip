a=[1,2,3,4,5,6,7,8,9,0]
k=5
l=[]
for i in range(len(a)):
	for j in range(len(a)):
		if(a[i]+a[j]==k and i!=j):
			li=[a[i],a[j]]
			print(li)
			li.sort()
			print(li)
			if li not in l:
				l.append(li)
print(l)
