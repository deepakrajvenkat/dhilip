st1=input()
s=list(st1)
for i in range(len(s)):
	if s[i]==' ' and s[i+1]==' ':
		s[i]=''
print("".join(s))
