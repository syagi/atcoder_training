A,K = map(int,input().split())

num=str(A)
numlen=len(num)
ans=float('inf')

for p in range(numlen):
    for q in range(10):
        for r in range(10):
            n=num[:p] # pまではAと同じ
            if len(set(n))>K:
                break
            n += str(q) + str(r) * (numlen-p-1)
            n = int(n)
            if len(set(str(n))) <= K:
                # print(n)
                ans = min(ans, abs(A-n))
        else:
            continue
        break
    else:
        continue
    break
print(ans)