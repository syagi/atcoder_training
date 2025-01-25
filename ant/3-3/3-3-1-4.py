# Segrent Tree
class IntervalError(Exception):
    def __init__(self):
        self.message = "Interval [a, b) must be a < b."

class SegmentTree:
    def __init__(self, size: int, op, init_value):
        self.size = size
        self.op = op
        self.init_value = init_value
        n = 2 ** ((size - 1).bit_length())
        treesize = n * 2
        st = [init_value] * treesize
        self.st = st
        self.offset = len(st) // 2

    @classmethod
    def from_sequence( cls, a, op, init_value):
        st = cls(len(a), op=op, init_value=init_value)
        for i, x in enumerate(a):
            st.set(i, x)
        return st

    def set(self, key: int, value):
        k = self.offset + key
        self.st[k] = value
        k >>= 1
        while k > 0:
            self.st[k] = self.op(self.st[k * 2], self.st[k * 2 + 1])
            k >>= 1

    def prod(self, a: int, b: int):
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
    
    def res(self,i):
        return self.st[i][0]+self.st[i][1]

def taco(a,b):
    return (a[0]*b[0], b[0]*a[1]+b[1])

N,M = map(int,input().split())

cmd = []
isActive = dict()
for i in range(M):
    p, a, b = map(float, input().split())
    p = int(p)
    isActive[p] = True
    cmd.append([p,a,b])

# 使う箱だけに圧縮する
actives = list(isActive.keys())
actives.sort()
actives = list(enumerate(actives))
transed = dict()
for i in range(len(actives)):
    transed[actives[i][1]]=actives[i][0]

segTaco = SegmentTree(len(actives), taco, (1,0))

best = 1
worst = 1

for i in range(M):
    p, a, b = cmd[i]
    p = transed[p]
    segTaco.set(p,(a,b))
    res = segTaco.res(1)
    best = max(best, res)
    worst = min(worst, res)

print(worst)
print(best) 