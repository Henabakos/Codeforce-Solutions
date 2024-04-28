import math 
for _ in range(int(input())):
    n, k = map(int, input().split())
    li = list(map(int, input().split()))
    stack=[]
    left=math.ceil(k/2)
    right=k//2
    for i in range(n):
        if left>=li[i]:
            left-=li[i]
            li[i]=0
        else:
            li[i]-=left
            break
    li.reverse()
    for j in range(n):
        if right>=li[j]:
            right-=li[j]
            li[j]=0
        else:
            li[j]-=right
            break
    print(li.count(0))
       

        
