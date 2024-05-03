import bisect

N,M=map(int,input().split())

P=[0]
for _ in range(N):
    pi=int(input())
    P.append(pi)

Q=[]
for i in P:
    for j in P:
        Q.append(i+j)

Q.sort()
# print(Q)

ans=0
for i in Q:
    j=bisect.bisect_left(Q,M-i)
    if(j>0):
        # print(i, j, Q[j-1])
        ans=max(ans,i+Q[j-1])
print(ans)