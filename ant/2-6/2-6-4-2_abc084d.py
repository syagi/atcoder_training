def primes(n):
    nums=[i for i in range(n+1)]

    nums[0]=nums[1]=0
    for i in range(2, int(n**0.5)+1):
        if nums[i]!=0:
            for j in range(i,n+1):
                if i*j >= n+1:
                    break
                nums[i*j]=0
    
    return nums

Q=int(input())
P=primes(10**5+1)
L=[]
R=[]
for _ in range(Q):
    l,r = map(int,input().split())
    L.append(l)
    R.append(r)

num2017=[0] * (max(R)+1)
for i in range(2,max(R)+1):
    if P[i]>0 and P[(i+1)//2]>0:
        num2017[i]=num2017[i-1]+1
    else:
        num2017[i]=num2017[i-1]

# print(num2017)
for i in range(Q):
    print(num2017[R[i]]-num2017[L[i]-1])
