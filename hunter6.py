n=input()
m=input().split(" ")
l=[]
flag=0
for i in range (len(m)):
	for j in range (len(m)):
		if (m[i]==m[j] and i!=j):
			flag+=1
			l.append(m[i])
if flag>=1:
	print(l[0])
else:
	print("unique")
  
