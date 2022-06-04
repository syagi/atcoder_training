h,w,x,y=map(int,input().split())

count=0
a=-0
b=h+1
for i in range(1,h+1):
    s=input()
    if i<x:
        if s[y-1]=='#':
            a=i
    elif i==x:
        # print(s[0:y])
        l=s[0:y].rfind('#')
        if l==-1:
            count += y
        else:
            count += y-1-l
        # print(l,count)
        # print(s[y:w])
        r=s[y:w].find('#')
        if r==-1:
            count += w-y
        else:
            count += r
        # print(r,count)
    elif i>x:
        if s[y-1]=='#':
            b=i
            break
count += x-a-1
# print(a,count)
count += b-x-1
# print(b,count)
print(count)