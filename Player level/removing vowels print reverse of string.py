N=str(raw_input())
list=['a','e','i','o','u']
n=[]
for i in N:
	if i not in list:
		n.append(i)
print n[::-1]
