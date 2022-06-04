n=int(input())

ret=0
for i in range(1,n+1):
    if not('7' in str(i) or '7' in str(oct(i))):
        ret += 1

print(ret)
