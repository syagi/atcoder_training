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
class IntervalError(Exception):
    def __init__(self):
        self.message = "Interval [a, b) must be a < b."

class SegmentTree:
    def __init__(self, size: int, op, init_value: int = 10 ** 8):
        self.size = size
        self.op = op
        self.init_value = init_value
        n = 2 ** ((size - 1).bit_length())
        treesize = n * 2
        st = [init_value] * treesize
        self.st = st
        self.offset = len(st) // 2

    @classmethod
    def from_sequence( cls, a, op, init_value: int = 10 ** 8):
        st = cls(len(a), op=op, init_value=init_value)
        for i, x in enumerate(a):
            st.set(i, x)
        return st

    def set(self, key: int, value: int):
        k = self.offset + key
        self.st[k] = value
        k >>= 1
        while k > 0:
            self.st[k] = self.op(self.st[k * 2], self.st[k * 2 + 1])
            k >>= 1

    def prod(self, a: int, b: int) -> int:
        a += self.offset
        b += self.offset - 1
        s = self.init_value
        while a < b:
            if a & 1:
                s = self.op(s, self.st[a])
                a += 1
            a >>= 1
            if not b & 1:
                s = self.op(s, self.st[b])
                b -= 1
            b >>= 1
        if a == b:
            s = self.op(s, self.st[a])
        return s


N,Q = map(int, input().split())

seglcm = SegmentTree(N+1, lcm, 1)
segsum = SegmentTree(N+1, add, 0)

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
    seglcm.set(x,t)
    s *= pow(t,-1,mod)
    s %= mod
    segsum.set(x,s)

for _ in range(Q):
    l,r = map(int,input().split())
    t = seglcm.prod(l,r+1)
    s = segsum.prod(l,r+1)

    ans = s*t
    ans %= mod
    print(ans)