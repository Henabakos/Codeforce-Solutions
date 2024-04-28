for _  in range(int(input())):
    li,t=input().split()
    s=input()
    a=s[::-1]
    cnt=0
    for i in range(len(a)):
        if a[i]==t:
            ind=i
            break
    s+=s
    dif=len(a)-ind-1
    for i in range(dif,len(s)):
        if s[i]!="g":
            cnt+=1
        else:
            break
    print(cnt)
            

