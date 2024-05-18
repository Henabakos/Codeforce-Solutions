for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    x=(sum(a))/len(a)
    if x==1:
        print(0)
    else:
        if sum(a)<0:
            print(1)
        elif sum(a)<n:
            print(1)
        else:
            

            print(abs(abs(sum(a))-n))