# for _ in range(int(input())):
#     li=list(input().split())
#     stack=["/"]
#     if li[0]=="pwa":
#         print("/".join(stack))
#     elif li[0]=="cd":
#         a=li[1].split("/")
#         print(a)
        
        
n = int(input())
stack = []
for _ in range(n):
    c = input().split()
    if c[0] == "pwd":
        p = "/"
        for d in stack:
            p += d + "/"
        print(p)
    else:
        p = c[1]
        if p[0] == "/":
            stack = []
            i = 1
        else:
            i = 0
        while True:
            j = p.find('/', i)
            if j != -1:
                d = p[i:j]
                if d != "..":
                    stack.append(d)
                else:
                    if stack:
                        stack.pop()
                i = j + 1
            else:
                d = p[i:]
                if d != "..":
                    stack.append(d)
                else:
                    if stack:
                        stack.pop()
                break