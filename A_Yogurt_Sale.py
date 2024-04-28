for _ in range(int(input())):
    n,a,b=map(int,input().split())
    modulo=n%2
    div=n//2
    min1=10000000000
    while(div>=0):
        min1=min(min1,div*b + modulo*a)
        div-=1
        modulo+=2
    print(min1)