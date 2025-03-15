import collections
# collection使うほうが楽かと思ったが無駄だった気もする

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

S=list(input())

#出現回数
C=collections.Counter(S)

#奇数のチェック
odd=False
for c in C.keys():
     if C[c]%2==1:
         odd_ch=c
         if odd:
             print("-1")
             exit(0)
         else:
             odd=True
# 出現位置 
ch_idxs = {}
for i in range(len(S))[::-1]:
    c = S[i]
    if c in ch_idxs:
        ch_idxs[c].append(i)
    else:
        ch_idxs[c] = [i]

p = []
# Left part
for i in range(len(S)):
    c = S[i]
    if C[c] - len(ch_idxs[c]) < C[c] // 2:
        p.append(ch_idxs[c].pop())
    if len(p) >= len(S) // 2:
        break

# Center part
if odd:
    p.append(ch_idxs[odd_ch].pop())

# right part
for i in range(len(S) // 2)[::-1]:
    c = S[p[i]]
    p.append(ch_idxs[c].pop())

bit = Bit(len(S))
ans = 0
for i, j in enumerate(p):
    ans += i - bit.sum(j+1)
    bit.add(j+1, 1)
print(ans)
