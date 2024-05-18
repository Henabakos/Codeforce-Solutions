for _ in range(int(input())):
    a1,a2,b1,b2=map(int,input().split())
    li=[1,2,3,4,5,6,7,8,9,10,11,12]
    dic={}
    for i in range(len(li)):
        dic[li[i]] = i
    li1=[min(a1,a2),max(a1,a2)]
    li2=[min(b1,b2),max(b1,b2)]
    a=dic[li1[0]]
    b=dic[li1[1]]
    c=dic[li2[0]]
    d=dic[li2[1]]
    finallist1=set(li[a:b+1])
    finallist2=set(li[c:c+1])
    if finallist1.intersection(finallist2):
        print("YES")
    else:
        print("NO")
