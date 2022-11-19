N,M = map(int,input().split())

path = [ [0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    path[a][b]=1
    path[b][a]=1

ans=0
from itertools import permutations

for p in permutations(range(1,N+1)):
    if p[0]==1:
        cnt = 0
        for i in range(N-1):
            if path[p[i]][p[i+1]] == 1:
                cnt += 1
            else:
                break
        else:
            ans += 1

print(ans)