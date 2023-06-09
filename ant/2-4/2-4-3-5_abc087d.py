N,M=map(int,input().split())

path=[ [] for _ in range(N)]

for _ in range(M):
    L,R,D=map(int,input().split())
    L-=1
    R-=1
    path[L].append((R,D))
    path[R].append((L,-D))

inf = 10**10
potencial = [inf]*N

from collections import deque

# 未評価の人v を0としたときの相対座標を総チェック
for v in range(N):
    if potencial[v]==inf:
        #BFS
        q = deque([v])
        potencial[v]=0
        while q:
            x = q.popleft()
            for y,d in path[x]:
                if potencial[y]<inf:
                    if potencial[y] != potencial[x]+d:
                        # yはxから距離dなので、矛盾
                        print("No")
                        exit()
                    continue
                potencial[y] = potencial[x]+d
                q.append(y)

print("Yes")

