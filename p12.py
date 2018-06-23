N,K=map(int,input().split())
A=input()
l=A.split(" ")
for i in range (K):
	l=l[N-1:]+l[0:N-1]
print (" ".join(l))	
