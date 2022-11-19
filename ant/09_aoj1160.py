def sweep_island(x,y):
    stack=[(x,y)]

    while len(stack) > 0:
        (x,y)=stack.pop()
        C[x][y]="0"

        for i,j in [[x, y+1],[x,y-1],[x-1,y],[x+1,y]]:
            if (i<0 or h<=i or j<0 or w<=j):
                continue
            elif C[i][j]=="0":
                continue
            else:
                stack.append((i,j))

w,h = map(int,input().split())

while h>0 and w>0:
    C=[[] for _ in range(h)]

    for i in range(h):
        C[i]=list(map(int,input().split()))

    ans=0
    for i in range(h):
        for j in range(w):
            if C[i][j]==1:
                sweep_island(i,j)
                ans += 1
    print(ans)
    w,h = map(int,input().split())