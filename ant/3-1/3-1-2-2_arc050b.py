R,B=map(int,input().split())
x,y=map(int,input().split())

def check(k):
    if R<k or B<k :
        return False
    elif ((R-k)//(x-1)+(B-k)//(y-1)) < k:
        return False
    return True

high = min(R,B)+1
low = 0

while abs(high-low) > 1:
    mid = (high+low) // 2
    if check(mid):
        low = mid
    else:
        high = mid

print(low)