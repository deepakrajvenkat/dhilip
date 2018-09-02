n=input()
m=input()
if(n>m):
	maximum=n
else:
	maximum=m
for i in range(1,maximum):
	if(n%i==0 and m%i==0):
		hcf=i
print(hcf)
