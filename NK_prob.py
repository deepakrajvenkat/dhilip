N=int(input())
K=int(input())
l=[]
for i in range(N):
	l.append(int(input()))
sum=0
for i in range(K):
	sum+=l[i]
print(sum)
