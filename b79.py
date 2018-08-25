x,y=input().split()
x=int(x)
y=int(y)
n=x*y
for i in range (100):
	s=i*i
	if (s==n):
		print("yes")
		break
	elif(s>n):
		print("no")
		break
