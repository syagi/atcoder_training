N=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))

from itertools import permutations

win=0
ptn=0

for a in permutations(range(N)):
    for b in permutations(range(N)):
        ptn+=1
        tmp_win=0
        tmp_lose=0
        for i in range(N):
            if A[a[i]]>B[b[i]]:
                tmp_win+=1
            else:
                tmp_lose+=1
        if tmp_win>tmp_lose:
            win+=1

print(win/ptn)
