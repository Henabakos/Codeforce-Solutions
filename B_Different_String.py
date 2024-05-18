for _ in range(int(input())):
    s=input()
    a=set(s)
    if len(a)==1:
        print("NO")
    else:
        print("YES")
        print(s[::-1])