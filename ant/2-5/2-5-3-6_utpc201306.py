class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

def kruskal(n, num, edges):
    uf = UnionFind(n)
    ret = 0
    used = []
    for s, t, c in edges:
        if not uf.same(s, t):
            uf.unite(s, t)
            ret += c
            used.append((s, t, c))
    if len(used) != num - 1:
        ret = "IMPOSSIBLE"
    return (ret, used)

N,M=map(int,input().split())

edges=[ {} for _ in range(N)]
for _ in range(M):
    u,v,w=map(int,input().split())
    edges[u][v]=w
    edges[v][u]=w

Q=int(input())

uf=UnionFind(N)
ans=[]


