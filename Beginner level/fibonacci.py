N=int(raw_input())
a=0
b=1
print(b)
for i in range(1,N):
	c=a+b
	a=b
	b=c
	print(c)
