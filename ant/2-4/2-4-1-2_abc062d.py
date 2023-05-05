import heapq

N=int(input())

A=list(map(int,input().split()))

ans=-10**30
for k in range(N, 2*N):
    left = list(map(lambda x:x*-1, A[:k]))
    right = A[k:]
    heapq.heapify(left)
    heapq.heapify(right)
    sum_left=0
    sum_right=0
    for i in range(N):
        sum_left+=heapq.heappop(left)
        sum_right+=heapq.heappop(right)
    
    ans=max(ans,-1*(sum_left+sum_right))

print(ans)
