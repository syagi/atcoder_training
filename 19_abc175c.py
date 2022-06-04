x,k,d=map(int,(input().split()))
x=abs(x)
if(x>=k*d):
    print(x-k*d)
elif((k-int(x/d))%2==0):
    print(abs(x-d*int(x/d)))
else:
    print(abs(x-d*int(x/d)-d))