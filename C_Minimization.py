n,k=map(int,input().split())
li=list(map(int,input().split()))
a=float("inf")
for i in range(k):
    min_ = min(li)
    if min_ == 0 or min_==a:
        print(0)
    else:
        print(min_)
        for j in range(len(li)):
            li[j]-= min_
            if li[j]==0:
                li[j]=a
            
    
