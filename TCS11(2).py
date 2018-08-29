s=input()
l=list(s)
for i in range(len(l)):
	if(l[i]=='a' or l[i]=='e' or l[i]=='i' or l[i]=='o' or l[i]=='u'):
		l[i]=l[i].upper()
ans="".join(l)
print(ans)
