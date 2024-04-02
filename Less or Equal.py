n,k=map(int,input().split())
li=list(map(int,input().split()))
li.sort()
if li[k]==li[k-1]:
    print(-1)
else:
    print(li[k-1])
