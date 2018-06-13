s=input()
s=s.split(" ")
if s[0].isdigit() and s[1].isdigit():
	n=int(s[0])
	m=int(s[1])
	n=n**m
	print(n)
else:
	print("Invalid input")
