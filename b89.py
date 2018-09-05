n=input()
l=list(n)
m=len(l)
for i in range(m):
	for j in range(m-i-1):
		if(l[j]>l[j+1]):
			temp=l[j]
			l[j]=l[j+1]
			l[j+1]=temp
ans="".join(l)
print(ans)
