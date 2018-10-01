n=input()
count1=0
count2=0
print(n[1])
for i in range(len(n)):
	if(n[i]=='('):
		count1+=1
	elif(n[i]==')'):
		count2+=1
print(count1,count2)
if(count1==count2):
	print("yes")
else:
	print("no")
