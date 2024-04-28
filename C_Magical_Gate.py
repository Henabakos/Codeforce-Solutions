from collections import defaultdict
for _ in range(int(input())):
    li=list(input().split())
    s=input()
    s+=s
    i,j=0,1
    n=len(s)
    _max=0
    if li[1] == "g":
        print(0)
        continue
    
    for _ in range(n):
        if s[i]==li[1]:
            # print(i,j,s[i])
            if s[j]=="g":
               _max=max(_max,j-i)
               i=j
            else:
                j+=1
        else:
            i+=1
            j+=1
    print(_max)




