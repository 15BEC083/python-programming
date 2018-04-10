M=[]
N,K=raw_input().split(' ')
n=int(N)
k=int(K)
for i in range(1,n+1):
	b=k**i
	M.append(b)
if N in M:
	print("yes")
else:
	print("no")
