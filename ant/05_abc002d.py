from itertools import combinations
from unittest import result

N,M = map(int,input().split())

pairs = []
for _ in range(M):
    pairs.append(tuple(map(int,input().split())))

ans = 0

for i in range(1<<N):
    group = []
    for j in range(N):
        if(i & (1<<j)):
            group.append(j+1)

    for pair in combinations(group,2):
        if (pair not in pairs):
            break
    else:
        ans = max(ans, len(group))

print(ans)
