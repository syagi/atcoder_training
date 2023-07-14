# 3部グラフか否かで解が変わる
# https://b1u3.hateblo.jp/entry/2019/11/27/215201
# 2部グラフの場合
#   黒*白-M
# 2部グラフでない場合
#   N(N-1)//2-M
import sys

# デフォルトだとRE
sys.setrecursionlimit(10000)

from collections import defaultdict

G=defaultdict(list)

N,M=map(int,input().split())

visited = [[False for _ in range(N)] for _ in range(5)]

for i in range(M):
    v,u = map(int, input().split())
    G[v-1].append(u-1)
    G[u-1].append(v-1)

# 2部グラフ判定
# -1 or 1 で色を塗る
COLORS = [0 for _ in range(N)]

def dfs(pos, color):
    global COLORS
    COLORS[pos]=color
    ans = True
    for dest in G[pos]:
        if COLORS[dest] == color:
            # 隣り合う同色がある
            return False
        elif COLORS[dest] == 0:
            ans &= dfs(dest, -color)
    return ans

if dfs(0,1):
    black = 0
    for i in COLORS:
        if i == -1:
            black +=1
    white = N-black
    print(black*white-M)
else:
    print(N*(N-1)//2-M)