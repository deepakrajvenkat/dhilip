l=input()
s=list(l)
for i in range(len(s)):
	x=ord(s[i])
	if(97<=x<=122):
		x=x-32
		s[i]=chr(x)
	elif(65<=x<=90):
		x=x+32
		s[i]=chr(x)
print("".join(s))
