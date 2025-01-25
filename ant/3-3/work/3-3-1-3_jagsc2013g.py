
mod = 10**9+7

def gcd(a,b):
    while a!=0:
        b%=a
        if b==0: return a
        a%=b
    return b

def lcm(a,b):
    return a*b//gcd(a,b)

def add(a,b):
    return (a+b) % mod

# Segrent Tree
# init_val:初期数列、 segfunc：評価用関数、 ide_ele：クエリの初期値
class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n-1).bit_length()
        self.tree = [ide_ele]*2*self.num
        for i in range(n):
            self.tree[self.num+i] = init_val[i]
        for i in range(self.num-1,0,-1):
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])

    # k番目にxを加算
    def add(self, k, x):
        k += self.num
        self.tree[k] += x
        while k>1:
            self.tree[k>>1] = self.segfunc(self.tree[k], self.tree[k^1])
            k >>= 1

    # k番目をxに置換
    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k>1:
            self.tree[k>>1] = self.segfunc(self.tree[k],self.tree[k^1])
            k >>= 1
    
    def query(self, l, r):
        res = self.ide_ele
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r&1:
                res = self.segfunc(res, self.tree[r-1])
            l >>= 1
            r >>= 1
        return res
    
N,Q = map(int, input().split())
    
seglcm = SegTree([1 for i in range(N+1)], lcm, 1)
segsum = SegTree([0 for i in range(N+1)], add, 0)

P = list(map(int,input().split()))

for x in range(1,N+1):
    s = 0
    t = 0
    y = x
    while True:
        y = P[y-1]
        s += y
        t += 1
        if y == x:
            break
    seglcm.update(x,t)
    s *= pow(t,-1,mod)
    s %= mod
    segsum.update(x,s)

for _ in range(Q):
    l,r = map(int,input().split())
    t = seglcm.query(l,r+1)
    s = segsum.query(l,r+1)

    ans = s*t
    ans %= mod
    print(ans)