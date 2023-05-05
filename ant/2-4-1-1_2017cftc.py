import heapq
N,K = map(int,input().split())

ab=[]

for _ in range(N):
    ai,bi=map(int,input().split())
    ab.append([ai,bi])
heapq.heapify(ab)

ans=0

for i in range(K):
    t=heapq.heappop(ab)
    ans+=t[0]
    heapq.heappush(ab,[t[0]+t[1],t[1]])

print(ans)

