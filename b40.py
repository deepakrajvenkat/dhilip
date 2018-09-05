n=int(input())
t1=0
t2=1
l=[]
for i in range(n):
	nt=t1+t2
	t1=t2
	t2=nt
	l.append(str(t1))
s=" ".join(l)
print(s)
