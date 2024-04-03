t=int(input())
for i in range(t):
    n=int(input())
    li=list(map(int,input().split()))
    for i ,j in enumerate(li):
        if li.count(j)==1:
            print(i+1)
            break