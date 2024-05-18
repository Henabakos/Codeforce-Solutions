from collections import defaultdict

for i in range(int(input())):
    n=int(input())
    stack=list(map(int,input().split()))
    res=[]
    a=defaultdict(int)
    for i in range(len(stack)):
        a[stack[i]]=i
    
    for i in range(len(stack)):
        if stack:
            max_= max(a)
            x=stack[a[max_] :]
            
            
            res.extend(x)
            stack=stack[:a[max_]]
            del a[max_]
            print
        else:
            break

    print(*res)