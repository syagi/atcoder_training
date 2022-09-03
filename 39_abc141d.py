n,m = map(int, input().split())

A=list(map(lambda x:-x,map(int,input().split())))


import heapq

heapq.heapify(A)

for i in range(m):
    x=heapq.heappop(A)
    x=int(x/2)
    heapq.heappush(A,x)

ans=-1*sum(A)

print(ans)