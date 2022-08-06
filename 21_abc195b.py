a,b,w = map(int,input().split())

w_g=w*1000
ans_max = -1
ans_min = 10**6+1
for x in range(1,10**6+1):
    if a*x <= w_g <= b*x:
        ans_min = min(ans_min,x)
        ans_max = max(ans_max,x)

if ans_min == 10**6+1:
    print("UNSATISFIABLE")
else:
    print(ans_min,ans_max)