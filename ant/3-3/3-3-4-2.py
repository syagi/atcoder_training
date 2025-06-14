# https://tjkendev.github.io/procon-library/python/math/baby-step-giant-step.html

# X^K ≡ Y (mod M) となるような K を求める
def solve(X, Y, M):
    D = {1: 0}

    sq = int(M**.5)+1

    # Baby-step
    Z = 1
    for i in range(sq):
        Z = Z * X % M
        D[Z] = i+1

    if Y in D:
        return D[Y]

    # Giant-step
    R = pow(Z, M-2, M) # R = X^(-sq)

    for i in range(1, sq+1):
        Y = Y * R % M
        if Y in D:
            return D[Y] + i*sq
    return -1

def main():
    X, P, A, B = map(int,input().split())

    if B >= A+P:
        return 1
    a,b = A%P, B%P

    if a>b:
        a,b = b,a
    
    if b-a <= 2**24:
        # 愚直に計算
        res = float('inf')
        for i in range(a,b+1):
            res = min(res, pow(X,i,P))
        return res
    else:
        for j in range(1,P):
            i = solve(X,j,P)
            if i<a:
                i+=P
            if a <= i <= b:
                return j

print(main())