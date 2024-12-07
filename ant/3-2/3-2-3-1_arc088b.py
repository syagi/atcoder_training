#参考 https://emtubasa.hateblo.jp/entry/2019/02/14/000000_2

S=list(map(int,input()))

ans=10**6
length=[]

i=0
while i<len(S):
    i+=1
    cnt = 1
    # 同じ数字の連続数をカウント
    while i<len(S) and S[i-1]==S[i]:
        cnt += 1
        i += 1
    length.append(cnt)

for i in range(1,len(length)) :
    length[i] += length[i-1]

for i in range(len(length)):
    ans = min(ans, max(length[i], len(S)-length[i]))

print(ans)