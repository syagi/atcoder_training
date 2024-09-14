N=int(input())

A=list(map(int,input().split()))

l=0
r=0
ans=0
t=0

while l<N:
    while r<N and t^A[r] == t + A[r]:
        t += A[r]
        r += 1
    ans += r-l 
    t -= A[l]
    l += 1

print(ans)

