import itertools

N,M,P,Q,R = map(int,input().split())

choco=[ []  for _ in range(N)]

for _ in range(R):
    x,y,z = map(int,input().split())
    x-=1
    y-=1
    choco[x].append((y,z))

ans=0
# 女子だけ総当たり  
for girls in itertools.combinations(range(N),P):
    score = [0] * M
    for x in girls:
        # 男子ごとにスコア計算
        for y,z in choco[x]:
            score[y] +=z
    score.sort(reverse=True)
    ans = max(ans, sum(score[:Q]))

print(ans)
