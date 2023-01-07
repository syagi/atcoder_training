freq=list(map(int,input().split(",")))
keysize=list(map(int,input().split(",")))

if len(freq)>sum(keysize):
    print(-1)
    exit()

freq.sort(reverse=True)

ans=0
keys=[ 0 for _ in range(len(keysize))]
for letter in freq:
    key_min=100
    key_min_index=-1
    #print(letter)
    #print(keys)
    for i,key in enumerate(keys):
        if key<key_min and keys[i]<keysize[i]:
           key_min_index=i
           key_min=key 
    else:
        #print(key_min_index,key_min)
        keys[key_min_index]+=1
        ans+=keys[key_min_index]*letter

print(ans)
