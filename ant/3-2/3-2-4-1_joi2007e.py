import copy
R,C = map(int,input().split())

s=[]
for i in range(R):
    s.append(list(map(int,input().split())))

res=0

# 横軸全てで総当たり
for b in range(2**R):
    s2=copy.deepcopy(s)
    for i in range(R):
        if b & (1<<i):
            for j in range(C):
                s2[i][j] = 1 - s2[i][j]
    # 縦軸の数え上げ
    num=0
    for i in range(C):
        tmp=0
        for j in range(R):
            if s2[j][i]==0:
                tmp+=1
        num += max(tmp, R-tmp)
    res=max(res,num)

print(res)
