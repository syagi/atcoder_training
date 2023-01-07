N=int(input())

stacks=[]
for _ in range(N):
    box_size=int(input()) 
#    print(box_size)
    if stacks:
        target_stack=-1
        target_stack_top=1000000
        for i, stack in enumerate(stacks):
            if box_size<=stack and stack<target_stack_top:
                target_stack=i
                target_stack_top=stack
#        print(target_stack,target_stack_top)
        if target_stack==-1:
            stacks.append(box_size)
        else:
            stacks[target_stack]=box_size
    else:
        stacks.append(box_size)
#    print(stacks)

print(len(stacks))