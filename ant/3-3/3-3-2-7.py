
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


N, M, H = map(int, input().split())
A = list(map(int, input().split()))

bit = Bit(N + M)
for i,a in enumerate(A,1):
    bit.add(i,a)

top = N
height = sum(A)
for _ in range(M):
    op, arg = input().split()
    arg = int(arg)
    if op=='add':
        A.append(arg)
        top +=1
        height += arg
        bit.add(top,arg)
    else:
        if height <= arg-H:
            print('miss')
        else:
            l,h = 1, top
            while l <= h:
                m = (l+h)//2
                if bit.sum(m) > arg - H:
                    h = m-1
                else:
                    l = m+1
            if height > bit.sum(l) < arg + H:
                print('stop')
            else:
                height -= A[l-1]
                bit.add(l,-A[l-1])
                print('go')