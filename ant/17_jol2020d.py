n=int(input())
k=int(input())

a=[]
for _ in range(n):
    a.append(input())

from itertools import permutations

b=[]

for v in permutations(list(range(n)),k):
    temp=""
    for i in range(k):
        temp+=a[v[i]]
    if temp not in b:
        b.append(temp)

print(len(b))
