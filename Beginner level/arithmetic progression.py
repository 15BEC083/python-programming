N=int(raw_input())
A=int(raw_input())
D=int(raw_input())
s=0
for i in range(1,N+1):
    g=A+(i-1)*D
    s=s+g
print(s)
