from wsgiref.simple_server import demo_app


n,a,b=map(int,input().split())
mod=10**9+7

def nCr_mod(n,r,mod):
    numeractor=1
    for i in range(n-r+1,n+1):
        numeractor = numeractor * i % mod
    denominator=1
    for i in range(1,r+1):
        denominator = denominator * i % mod
    
    deno_inv = pow(denominator,-1,mod)
    
    return numeractor*deno_inv%mod

ans=(pow(2,n,mod)-nCr_mod(n,a,mod)-nCr_mod(n,b,mod)-1)%mod

print(ans)