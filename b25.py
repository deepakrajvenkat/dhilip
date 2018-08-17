m=input()
n=input().split()
n.sort()
l=len(n)
if(l%2 !=0):
	i=l//2
	print(n[i])
else:
	s=(int(n[j])+(int(n[j+1]))//2)
	print(s)
