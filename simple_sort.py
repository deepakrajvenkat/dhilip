n=int(input())
s=input()
l=s.split()
length_list=len(l)
if length_list==n:
	l.sort()
	print(l)
else:
	print ("invalid input")

