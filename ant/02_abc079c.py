S=list(map(int,list(input())))

for i in range(1<<3):
    subtotal = S[0]
    ans=str(S[0])
    for j in range(3):
        if(i & (1 << j)):
            subtotal += S[j+1]
            ans=ans+'+'+str(S[j+1])
        else:
            subtotal -= S[j+1]
            ans=ans+'-'+str(S[j+1])
#    print(subtotal)
#    print(ans)
    if(subtotal==7):
        print(ans+'=7')
        exit()