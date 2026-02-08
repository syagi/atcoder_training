V,E = map(int,input().split())

# flow[u][v] : uからvまでの最大流量
flow = [[0 for _ in range(V)] for _ in range(V)]

for i in range(E):
    u,v,c = map(int,input().split())
    flow[u][v]=c

def dfs(src, dest, cap):
    if src == dest:
        return cap
    used[src] = True
    for to in range(V):
        if not used[to] and flow[src][to] > 0:
            actual_flow = dfs(to, dest, min(cap, flow[src][to])) 
            if actual_flow > 0:
                flow[src][to] -= actual_flow
                flow[to][src] += actual_flow
                return actual_flow
    return 0
        
ans = 0
while True:
    used = [False for _ in range(V)]
    f = dfs(0, V-1, 10000)
    if f==0:
        break
    ans += f

print(ans)



