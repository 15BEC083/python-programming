n=int(raw_input())
prime=0
for i in range(2,n/2,1):
	if n%i==0:
		prime=prime+1

if (prime<=0):
	print("yes")
else:
	print("no")
