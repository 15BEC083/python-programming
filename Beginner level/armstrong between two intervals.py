M=int(raw_input())
N=int(raw_input())
sum=0
for i in range(M,N):
	temp=i
	while(i<0):
		d=i%10
		sum=sum+(d**3)
		i=i//10
	if(temp==sum):
		print(sum)
