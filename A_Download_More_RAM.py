for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    f={}
    fb={}
    for ind,value in enumerate(a):
        f[ind]=value
    for ind,value in enumerate(b):
        fb[ind]=value
    f=sorted(f.items(),key=lambda x:x[1])
    a.sort()
    for i in range(n):
        if a[i]<=k:
            k+=b[f[i][0]]
            
        else:
            break
    print(k)