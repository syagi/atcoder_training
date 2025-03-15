from sortedcontainers import SortedSet

Q=int(input())
S=SortedSet([])
for i in range(Q):
  t,x = map(int,input().split())
  if t==1:
    S.add(x)
  else:
    print(S.pop(x-1))
