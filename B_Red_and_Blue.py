for _ in range(int(input())):
    pre1 = pre2 = max1 = max2 = 0
    n = int(input())
    li1 = list(map(int,input().split()))
    k = int(input())
    li2 = list(map(int,input().split()))
    for j in li1:
        pre1 += j
        max1 = max(pre1,max1)
    for i in li2:
        pre2 += i
        max2 = max(pre2,max2)
    print(max1 + max2)