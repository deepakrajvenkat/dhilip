word1=input()
word2=input()
L1=len(word1)
L2=len(word2)
if(word1==word2):
	print("1")
elif(L1==L2):
	NL1=[]
	for i in range (L1):
		if (word1[i]!=word2[i]):
			NL1.append(word1[i])
	
	print(len(NL1))
elif(L1>L2):
	NL2=[]
	N=L1-L2
	print(N)
	for j in range (L2):
		if (word1[j]!=word2[j]):
			NL2.append(word1[j])
	print(len(NL2))
	print(NL2)
elif(L1<L2):
	print(L2)
	
