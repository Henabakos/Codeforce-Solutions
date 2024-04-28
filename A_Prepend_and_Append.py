for _ in range(int(input())):
    n=int(input())
    s=input()
    i,j=0,n-1
    while i<=j:
        if s[i]!=s[j]:
            i+=1
            j-=1
            n-=2
        else:
            break
    print(n)