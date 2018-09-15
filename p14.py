s=input()
n=input()
m=list(n)
l=[]
for i in range(len(m)):
	if(m[i]=='a' or m[i]=='e' or m[i]=='i' or m[i]=='o' or m[i]=='u'):
		continue
	else:
		l.append(m[i])
s="".join(l)
print(s[::-1])
