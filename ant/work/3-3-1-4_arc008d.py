# https://qiita.com/recuraki/items/1f7d6c5e8559bfa43322

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

    # k番目をxに置換
    def update(self, k, x):
        k += self.num - 1
        self.tree[k] = x
        while k>0:
            k = (k-1)//2
            self.tree[k] = self.segfunc(self.tree[k*2+1],self.tree[k*2+2])
        # print(self.tree)
    
    def res(self):
        return self.tree[0][0] + self.tree[0][1]

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

initTree = [(1,0)] * (len(actives)+10)
segTaco = SegTree(initTree, taco, (1,0))

best = 1
worst = 1

for i in range(M):
    p, a, b = cmd[i]
    p = transed[p]
    segTaco.update(p,(a,b))
    res = segTaco.res()
    best = max(best, res)
    worst = min(worst, res)

print(worst)
print(best)
