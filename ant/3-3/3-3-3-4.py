# https://imoz.jp/algorithms/imos_method.html
# https://atcoder.jp/contests/code-festival-2015-final-open/submissions/59760560
N=int(input())
ST = [list(map(int,input().split())) for _ in range(N)]

A = set()
for s,t in ST:
    A.add(s)
    A.add(t)

# 座標圧縮 
serialized = {v: i for i,v in enumerate(sorted(A))}
ST = [(serialized[s], serialized[t]) for s,t in ST]

n = len(A)
table = [0] * n
l = 0
s0=t0=0

# imos
for s,t in ST:
    table[s] +=1
    table[t] -=1
    # N-1 なので除くべきもの（一番重なりがおおいボタン）を記録 
    if t-s>l:
        s0,t0=s,t
        l=t-s
# 除外 
table[s0] -=1
table[t0] +=1

for i in range(1,n):
    table[i] += table[i-1]

print(max(table))
