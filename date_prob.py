d1,m1,y1=map(int,input().split("/"))
d2,m2,y2=map(int,input().split("/"))
s=0
if(y1==y2 and m1==m2):
	print(d2-d1)
elif(y1=y2 and m1!=m2):
	if(y1%4==0 or y1%400==0 and y1%100!=0):
	month1=[31,29,31,30,31,30,31,31,30,31,30,31]
	x=month1[m1-1]
	for j in range(m1,12+1):
		s=s+month1[j-1]
	s=s-d1
	print(s)
else:
	month2=[31,28,31,30,31,30,31,31,30,31,30,31]
	x=month2[m1-1]
	for k in range(m1,12+1):
		s=s+month2[k-1]
	s=s-d1
	print(s)
	
for i in range(y1+1,y2):
	if(i%4==0 or i%400==0 and i%100!=0):
		s=s+366
	else:
		s=s+365
print(s)
#month
if(y1%4==0 or y1%400==0 and y1%100!=0):
	month1=[31,29,31,30,31,30,31,31,30,31,30,31]
	x=month1[m1-1]
	for j in range(m1,12+1):
		s=s+month1[j-1]
	s=s-d1
else:
	month2=[31,28,31,30,31,30,31,31,30,31,30,31]
	x=month2[m1-1]
	for k in range(m1,12+1):
		s=s+month2[k-1]
	s=s-d1
print(s)
if(y2%4==0 or y2%400==0 and y2%100!=0):
	month3=[31,29,31,30,31,30,31,31,30,31,30,31]
	for j in range(1,m2+1):
		s=s+month3[j-1]
	s=s-month3[m2-1]
else:
	month4=[31,28,31,30,31,30,31,31,30,31,30,31]
	x=month4[m2-1]
	for k in range(1,m2+1):
		s=s+month4[k-1]
	s=s-month4[m2-1]

print(s)
#date
s=s+(d2-d1)
print(s)
