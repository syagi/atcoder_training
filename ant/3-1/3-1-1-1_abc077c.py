import bisect

N=int(input())
A=sorted(list(map(int,input().split())))
B=sorted(list(map(int,input().split())))
C=sorted(list(map(int,input().split())))

ans=0
for i in range(N):
    a=bisect.bisect_left(A,B[i])
    c=N-bisect.bisect_right(C,B[i])
    ans+=a*c

print(ans)