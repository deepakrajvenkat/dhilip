l=list(n)
l2=[]
for i in range(len(l)):
	s=ord(l[i])
	s=s+3
	if(s>65 and s<90):
		p=chr(s)
		l2.append(p)
	if(s>90 and s<97):
		s=s-26
		p=chr(s)
		l2.append(p)
	if(s>97 and s<122):
		p=chr(s)
		l2.append(p)
	if(s>122):
		s=s-26
		p=chr(s)
		l2.append(p)
print("".join(l2))
