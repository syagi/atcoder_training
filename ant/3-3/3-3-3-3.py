# https://atcoder.jp/contests/joisc2016/submissions/59727224
class BIT:
    def __init__(self, n):
        self.size = n
        self.bit = [0] * (n + 1)
    def sum(self, i):
        r = 0
        while i > 0:
            r += self.bit[i]
            i -= i & -i
        return r
    def add(self, i, x):
        while i <= self.size:
            self.bit[i] += x
            i += i & -i

N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
Q = [list(map(int, input().split())) for _ in range(M)]

#print(A)
#print(Q)
B = set(A + [v[0] if t == 1 else v[1] for t, *v in Q])
#print(B)
S = {v: i for i, v in enumerate(sorted(B, reverse=True), 1)}
#print(S)

bit = BIT(len(S))
for i in range(N):
    bit.add(S[A[i]], 1)
    if i < N - 1:
        bit.add(S[min(A[i], A[i+1])], -1)

for t, *v in Q:
    if t == 1:
        b, = v
        print(bit.sum(S[b]))
    else:
        c, d = v
        i = c - 1
        bit.add(S[A[i]], -1)
        bit.add(S[d], 1)
        if c > 1:
            bit.add(S[min(A[i], A[i-1])],  1)
            bit.add(S[min(d, A[i-1])], -1)
        if c < N:
            bit.add(S[min(A[i], A[i+1])],  1)
            bit.add(S[min(d, A[i+1])], -1)
        A[i] = d