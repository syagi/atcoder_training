N,Q = map(int,input().split())
A=list(map(int,input().split()))
X=list(map(int,input().split()))


for i in range(Q):
    ans=0
    right = 0
    sum = 0
    for left in range(N):
        while right < N and sum + A[right] <= X[i]:
            sum += A[right]
            right += 1
        ans += (right - left)

        if right==left:
            right+=1
        else:
            sum -= A[left]
    print(ans)