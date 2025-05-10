class SegTree:
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2

        self.tree = [0] * (2*self.size-1)
        self.lazy = [0] * (2*self.size-1)
    
    def push(self,i,l,r):
        if self.lazy[i] != 0:
            self.tree[i] = (r-l)-self.tree[i]
            if r-l > 1:
                self.lazy[i*2+1] ^= self.lazy[i]
                self.lazy[i*2+2] ^= self.lazy[i]
            self.lazy[i]=0

    def update(self, s, t, i=0, l=0,r=None):
        if r==None:
            r=self.size
        self.push(i,l,r)

        if t <= l or s >= r:
            return
        if s <= l and t >=r:
            self.lazy[i]=1
            self.push(i,l,r)
        else:
            m = (l+r)//2
            self.update(s, t, i*2+1, l, m)
            self.update(s, t, i*2+2, m ,r)
            self.tree[i] = self.tree[i*2+1]+self.tree[i*2+2]

    def query(self, s, t, i=0, l=0, r=None):
        if r==None:
            r=self.size

        self.push(i,l,r)

        if t <= l or s >= r:
            return 0
        if s <= l and t >= r:
            return self.tree[i]
        
        m = (l+r)//2
        vl = self.query(s, t, 2*i+1, l, m)
        vr = self.query(s, t, 2*i+2, m, r)
        return vl+vr

n,Q = map(int,input().split())
st = SegTree(n)

for _ in range(Q):
    q,l,r = map(int,input().split())

    if q==1:
        st.update(l,r)
    else:
        ans = st.query(l,r)
        print(ans)