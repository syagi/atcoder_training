S=input()

ans=0

for i in range(1 << (len(S)-1)):
    subtotal=0
    subset=int(S[0])
    for j in range(len(S)-1):
        # print(subset,subtotal)
        if(i & (1<<j)):
            subtotal+=subset
            subset=0
        subset=subset*10+int(S[j+1])
    subtotal+=subset
    # print(subtotal)
    ans+=subtotal

print(ans)

