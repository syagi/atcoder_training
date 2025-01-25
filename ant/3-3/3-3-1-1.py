
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
   
n,q = map(int,input().split())

INF=2**31-1

st = SegmentTree(n,min,INF)

for _ in range(q):
    com,x,y = map(int,input().split())
    if com==0:
        st.set(x,y)
    elif com==1:
        ans=st.prod(x,y+1)
        print(ans)