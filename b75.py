s=input()
st=list(s)
l=len(s)
if (l%2==0):
	p=l//2
	st[p]='*'
	st[p-1]='*'
	st="".join(st)
	print(st)
else:
	p=l//2
	st[p]='*'
	st="".join(st)
	print(st)
