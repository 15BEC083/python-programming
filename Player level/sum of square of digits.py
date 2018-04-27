N=int(raw_input())
temp=N
sum=0
while (temp>0):
	d=temp%10
	sum=sum+(d**2)
	temp=temp//10
	
print(sum)
