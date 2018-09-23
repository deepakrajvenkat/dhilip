n=input().split()
for i in range(len(n)):
	s=n[i]
	rev=""
	for j in s:
		rev=j+rev
		n[i]=rev
print(n)
