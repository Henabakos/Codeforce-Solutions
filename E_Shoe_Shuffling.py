for _ in range(int(input())):
    n = int(input())
    s =list(map(int,input().split()))
    p = list(range(1, n+1))
    ans = True
    left, right = 0, 0
    
    while right < n:
        while right < n - 1 and s[right] == s[right+1]:
            right += 1
        if left == right:
            ans = False
        else:
            p[left:right+1] = p[left:right+1][-1:] + p[left:right+1][:-1]
        left = right + 1
        right += 1
    if ans :
        print(*p)
    else:
        print(-1)