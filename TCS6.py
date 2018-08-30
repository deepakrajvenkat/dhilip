import math
n=input()
flag=0
for i in range(2,n):
	if(n%i==0):
		flag=flag+1
if (flag==0):
	s=math.sqrt(n)
	print(round(s,2))
else:
	print("0.00")
