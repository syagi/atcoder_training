while True:
    n,m,l,s,t = map(int,input().split())
    if n==0:
        break

    # 全駅のグラフ
    G = [ set() for _ in range(n)]

    for _ in range(m):
        a,b,c = map(int,input().split())
        G[a-1].add((b-1, c))
        G[b-1].add((a-1, c))
        
    import heapq

    # 最短距離
    C = [[1<<60]*n for _ in range(n)]

    for i in range(n):
        C[i][i] = 0
        queue = [(0,i)]
        while queue:
            cost, v = heapq.heappop(queue)
            if C[i][v]!=cost: continue
            for v_, cost_ in G[v]:
                if cost + cost_ < C[i][v_]:
                    C[i][v_] = cost+cost_
                    heapq.heappush(queue, (cost+cost_, v_))

    # SIROのある駅
    J = []
    for _ in range(l):
        j,e = map(int,input().split())
        J.append((j-1,e))
    
    # dp[i][S]: Sまで訪問してiにいるときの時間
    dp = [[1<<60]*2**l for _ in range(l)]
    s -= 1
    for i in range(l):
        # 1件目
        dp[i][1<<i] = C[s][J[i][0]]+J[i][1]
    ans = 0
    for i in range(1<<l):
        for k in range(l):
            if i>>k&1==0:
                continue
            k_ = J[k][0]
            if dp[k][i]+C[k_][s] <= t:
                # 訪問件数カウント
                ans = max(ans, i.bit_count())
            for j in range(l):
                if i>>j&1: 
                    continue
                j_ = J[j][0]
                dp[j][i|1<<j] = min(dp[j][i|1<<j], dp[k][i]+C[k_][j_]+J[j][1])
    print(ans)
