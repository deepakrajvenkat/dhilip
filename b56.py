s=input()
count=0
for i in s:
	if(i.isalpha()):
		count+=1
	elif(i.isnumeric()):
		count+=1
if (count==len(s)):
	print("Yes")
else:
	print("No")
