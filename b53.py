n=int(input())
l=[]
sum=0
while(n>0):
	digit=n%10
	n=n//10
	sum+=digit
print(sum)
