import copy
H=10
W=10

A=[[] for _ in range(11)]
land=[]
sea=[]

for i in range(H):
    A[i]=list(input())
    for j in range(W):
        if A[i][j]=="o":
            land.append([i,j])
        else:
            sea.append([i,j])

def find_land(a):
    for i in range(H):
        for j in range(W):
            if a[i][j]=="o":
                return i,j
    return -1,-1

def is_island(a):
    stack = [find_land(a)]

    while len(stack) > 0:
        (x,y)=stack.pop()
        a[x][y]="x"

        for i,j in [[x, y+1],[x,y-1],[x-1,y],[x+1,y]]:
            if (i<0 or H<=i or j<0 or W<=j):
                continue
            elif a[i][j]=="x":
                continue
            else:
                stack.append((i,j))
            
    return find_land(a) == (-1,-1)
    
for x,y in sea:
    a = copy.deepcopy(A)
    a[x][y]="o"
    if is_island(a):
        print("YES")
        exit()
print("NO")

