for _ in range(int(input())):
    n = int(input())
    li1=list(map(int,input().split()))
    li2=list(map(int,input().split()))
    li=[li2[0] - li1[0]]
    left = 0 
    right = 1
    while (right < len(li1)):
        if li1[right] > li2[left]:
            left +=1
            li.append(abs(li1[left] - li2[right]))
            right += 1
        else:
            li.append(abs(li2[right] - li2[left]))
            left += 1
            right += 1
    print(*li)
