N=input()
fact=1
if(N<=20):
	for i in range(1,N):
		fact=fact*N
		N=N-1
	print(fact)
