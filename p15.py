n=input()
check=[]
maxi=1
for i in range(len(n)):
	count=0
	if n[i] in check:
		continue
	check.append(n[i])
	for j in range(len(n)):
		if(n[i]==n[j]):
			count=count+1
		if(count>maxi):
			maxi=count
			character=n[i]
print(character)	
