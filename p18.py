n=int(input())
l=[]
for i in range (n):
	l.append(input())
s="kabali"
count=0
s="".join(sorted(s))
for i in l:
	if(len(s)==len(i)):
		i="".join(sorted(i))
		if(s==i):
			count=count+1
print(count)
