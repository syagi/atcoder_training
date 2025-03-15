# https://atcoder.jp/contests/joi2011ho/submissions/36181795
from heapq import *
n = int(input())
q = []
ans = s = 0
for a, b in sorted(list(map(int, input().split())) for _ in range(n)):
    heappush(q, (b, a))
    s += a
    while q and s > q[0][0] * len(q):
        s -= heappop(q)[1]
    ans = max(ans, len(q))
print(ans)