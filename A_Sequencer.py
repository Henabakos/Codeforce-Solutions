for _ in range((int(input()))):
    n = int(input())
    li=list(map(int,input().split()))
    li2=[]
    left,right = 0 , len(li)-1
    while left < right:
        li2.append(li[left])
        li2.append(li[right])
        right -= 1
        left += 1
    if n%2 !=0:
        li2.append(li[left])
    print(*li2)
