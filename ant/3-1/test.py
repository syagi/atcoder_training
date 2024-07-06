from memory_profiler import profile
@profile
def test():
    N,M=1000,2*10**8
    P=[0]
    for _ in range(N):
        pi=N*N
        P.append(pi)

    Q=[]
    for i in P:
        for j in P:
            Q.append(i+j)

    Q.sort()
    # print(Q)

    ans=0
    for i in Q:
        j=bisect.bisect_left(Q,M-i)
        if(j>0):
            # print(i, j, Q[j-1])
            ans=max(ans,i+Q[j-1])
    print(ans)

test()