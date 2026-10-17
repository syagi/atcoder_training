Xa, Ya, Xb, Yb, Xc, Yc = map(float,input().split())

ans =  abs((Xb - Xa) * (Yc - Ya) - (Yb - Ya) * (Xc - Xa)) / 2
print(ans)