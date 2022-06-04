import math

n=int(input())

a=[]
for i in range(1,n+1):
    if(math.sqrt(n)<i):
        break
    if(n%i==0):
        a.append(i)
        if i!=int(n/i):
            a.append(int(n/i))

for i in sorted(a):
    print(i)
