s=input()
vowel=['a','e','i','o','u','A','E','I','O','U']
count=0
for  i in s:
	if i in vowel:
		count+=1
if(count==0):
	print("no")
else:
	print("yes")
