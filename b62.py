n=input()
l=['0','1']
flag=0
for i in range (len(n)):
	if n[i] in l:
		flag+=1
	else:
		flag=0
		break
if flag==0:
	print ("no")
else:
	print("yes")
