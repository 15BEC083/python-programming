N=int(raw_input())
prime=0
for i in range(2,N/2,1):
	if N%i==0:
		prime=prime+1

if (prime<=0):
	print("yes")
else:
	print("no")
