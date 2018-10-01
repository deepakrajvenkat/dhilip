n=input()
count1=0
count2=0
for i in range(len(n)):
	if(n[i]=='('):
		count1+=1
	elif(n[i]==')'):
		count2+=1
if(count1==count2):
	print("yes")
else:
	print("no")
