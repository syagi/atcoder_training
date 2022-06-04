n=int(input())

s1,t1=input().split()
si,ti=input().split()
if int(ti)>int(t1):
    s2=s1
    t2=t1
    s1=si
    t1=ti
else:
    s2=si
    t2=ti

for i in range(n-2):
    si,ti=input().split()
    if int(ti)>int(t1):
        s2=s1
        t2=t1
        s1=si
        t1=ti
    elif int(ti)>int(t2):
        s2=si
        t2=ti

print(s2)
