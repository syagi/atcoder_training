A,K = map(int,input().split())

num=str(A)
numlen=len(num)
ans=float('inf')

for p in range(1,numlen):
    for q in range(10):
        for r in range(10):
            n=num[:p] # pまではAと同じ
            if len(set(n))>K:
                break
            n += str(q) + str(r) * (numlen-p-1)
            if len(set(n)) <= K:
                # print(n)
                ans = min(ans, abs(A-int(n)))
        else:
            continue
        break
    else:
        continue
    break
print(ans)