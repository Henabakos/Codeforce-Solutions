for _ in range(int(input())):
    a=[1,2,3,4,5,6,7,8,9,0]
    li=list(map(int,input()))
    index1,cnt=0,0
    for i in li:
        f=a.index(i)
        max1=max(f,index1)
        min1=min(f,index1)
        cnt=cnt+(max1-min1+1)
        index1=f
    print(cnt)


