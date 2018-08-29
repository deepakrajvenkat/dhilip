s=input()
l=list(s)
for i in range(len(l)):
	if(l[i]=='a' or l[i]=='e' or l[i]=='i' or l[i]=='o' or l[i]=='u'):
		a=ord(l[i])-32
		l[i]=chr(a)
ans="".join(l)
print(ans)
