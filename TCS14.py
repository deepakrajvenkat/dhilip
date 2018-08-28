t1=0
t2=1
for i in range (10):
	nt=t1+t2
	t1=t2
	t2=nt
	if(t1<10):
		print(t1)
