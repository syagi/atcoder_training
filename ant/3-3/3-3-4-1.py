# https://sigma1113.hatenablog.com/entry/2020/12/15/225256
Q=int(input())

D=int(pow(200000,0.5))
b=[ [] for _ in range(D+1)] # √Q個のブロックに分割
for _ in range(Q):
    t,x = map(int,input().split())
    if t==1:
        i = x//D # 該当ブロックを決定
        j = 0
        l = len(b[i])
        while j<l:  # ブロック内で挿入箇所特定
            if b[i][j]>x:
                break
            j += 1
        b[i].insert(j,x)

    else:
        cnt = 0
        for i in range(D+1): # 該当ブロックを特定
            l = len(b[i])
            if cnt+l >= x:
                break
            cnt += l
        j = x - cnt - 1
        print(b[i][j])
        del b[i][j]
