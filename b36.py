s=input()
count=0
for i in s:
	if(i=='!' or i=='@' or i=='#' or i=='$' or i=='%' or i=='^' or i=='&' or i=='*' or i=='_'):
		count+=1
print(count)
