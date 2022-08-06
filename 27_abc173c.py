h,w,k = map(int, input().split())

c=[]

for row in range(h):
    c.append(list(input()))

ans=0

for row_r in range(1<<h):
    for col_r in range(1<<w):
        black=0

        for row in range(h):
            for col in range(w):
                if (row_r>>row & 1)==0 and (col_r>>col & 1)==0:
                    if c[row][col]=="#":
                        black+=1
        if black==k:
            ans+=1
print(ans)
        
