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
H=list(map(int,input().split()))

#座標圧縮
S=sorted(list(set(H)))
if (len(A)!=len(S)):
    print("-1")
    exit(0)

rank = {x:i+1 for i,x in enumerate(S)}
B=[]
for h in H:
    B.append((rank[h],h))
# print(H)
# print(B)
bit = Bit(len(B))
ans = 0
for i,(b,h) in enumerate(B):
    ans += (i-bit.sum(b))*h
    bit.add(b,1)

print(ans)