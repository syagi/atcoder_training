# https://ikatakos.com/pot/programming_algorithm/dynamic_programming/inversion

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
  
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
  
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

N=int(input())
A=list(map(int,input().split()))

bit = Bit(N)
ans = 0

for i,a in enumerate(A):
    ans += i-bit.sum(a)
    bit.add(a,1)

print(ans)