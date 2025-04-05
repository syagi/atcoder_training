# https://mikami3345.cloudfree.jp/AOJ_Solutions/DSL/DSL_2_Solutions.html
class SegTree:
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2

        self.tree = [0] * (2*self.size-1)
        self.lazy = [0] * (2*self.size-1)
    
    def update(self, s, t, x, i=0, l=0,r=None):
        if r==None:
            r=self.size
        
        if self.lazy[i] != 0:
            self.tree[i] += self.lazy[i]*(r-l)
            if 2*i+2 < len(self.tree):
                self.lazy[2*i+1] += self.lazy[i]
                self.lazy[2*i+2] += self.lazy[i]
        self.lazy[i]=0

        if t <= l or s >= r:
            return 0

        if s <= l and t >=r:
            self.tree[i] += x*(r-l)

            self.lazy[i]=0
            if 2*i+2 < len(self.tree):
                self.lazy[2*i+1] += x
                self.lazy[2*i+2] += x
            return self.tree[i]

        m = (l+r)//2
        vl = self.update(s,t,x, 2*i+1, l, m)
        vr = self.update(s,t,x, 2*i+2, m, r)
        self.tree[i] = self.tree[2*i+1] + self.tree[2*i+2]

    def sum(self, s, t, i=0, l=0, r=None):
        if r==None:
            r=self.size

        if self.lazy[i] !=0:
            self.tree[i] += self.lazy[i]*(r-l)
            if 2*i+2 < len(self.tree):
                self.lazy[2*i+1] += self.lazy[i]
                self.lazy[2*i+2] += self.lazy[i]
            self.lazy[i] = 0
        
        if t <= l or s >= r:
            return 0
        if s <= l or t >= r:
            return self.tree[i]
        
        m = (l+r)//2
        vl = self.sum(s,t, 2*i+1, l, m)
        vr = self.sum(s,t, 2*i+2, m, r)
        return vl+vr

n,q = map(int,input().split())
seg_tree = SegTree(n)

for _ in range(q):
    query = list(map(int,input().split()))
    if query[0] == 0:
        _,s,t,x = query
        seg_tree.update(s-1,t,x)
    else:
        _,s,t = query
        result = seg_tree.sum(s-1,t)
        print(result)