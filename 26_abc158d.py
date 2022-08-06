from ast import Not
from collections import deque

S=input()
q=int(input())

rev=False
s=deque()

for i in range(len(S)):
  s.append(S[i])

for i in range(q):
  query=list(map(str,input().split()))

  if query[0]=="1":
    rev = not rev
  else:
    if inv:
      if query[1]=="1":
        s.append(query[2])
      else:
        s.appendleft(query[2])
    else:
      if query[1]=="1":
        s.appendleft(query[2])
      else:
        s.append(query[2])

ret="".join(s)

if inv:
  ret=ret[::-1]

print(ret)