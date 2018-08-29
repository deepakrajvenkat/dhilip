n=input()
for i in range(100):
	a=i*i
	if (a==n):
		print("perfect square")
		break
	elif(a>n):
		print("not perfect square")
		break
