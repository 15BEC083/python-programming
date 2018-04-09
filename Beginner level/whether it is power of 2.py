M=[]
N=int(raw_input())
for i in range(1,N+1):
	b=2**i
	M.append(b)
if N in M:
	print("yes")
else:
	print("no")
