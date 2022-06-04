n,k = map(int,input().split())

ai=n
for i in range(k):
    #print(ai)
    ai_sorted=list(sorted(str(ai)))
    #print(ai_sorted)
    g1i = int(''.join(reversed(ai_sorted)))
    #print(g1i)
    g2i = int(''.join(ai_sorted))
    #print(g2i)
    ai = g1i-g2i
print(ai)