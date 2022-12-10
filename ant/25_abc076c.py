S=list(input())
T=list(input())

ans_list=[]

def solve(start):
    ans=""
    for i in range(start):
        if(S[i]=="?"):
            ans+="a"
        else:
            ans+=S[i]
    for i in range(start,len(S)):
        #print("dbg:",ans)
        if(S[i]==T[0] or S[i]=="?"):
                if(len(S)-i<len(T)):
                    return "UNRESTORABLE",-1
                for j in range(1,len(T)):
                    if((S[i+j]==T[j]) or (S[i+j]=="?")):
                        continue
                    else:
                        if(S[i]=="?"):
                            ans+="a"
                        else:
                            ans+=S[i]
                        break
                else:
                    ans+="".join(T)
                    if(len(S)-i>len(T)):
                        for k in range(i+len(T),len(S)):
                            if(S[i]=="?"):
                                ans+="a"
                            else:
                                ans+=S[i]
                    return ans,i+1
        else:
            if(S[i]=="?"):
                ans+="a"
            else:
                ans+=S[i]
    else:
        return "UNRESTORABLE",-1


pos=0
while 0<=pos:
    tmp_ans,pos = solve(pos)
    #print("dbg:",tmp_ans,pos)
    if tmp_ans=="UNRESTORABLE":
        if ans_list==[]:
            print(tmp_ans)
            exit()
        else:
            break
    else:
        ans_list.append(tmp_ans)

print(min(ans_list))