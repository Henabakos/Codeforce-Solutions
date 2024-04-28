from collections import deque
for _ in range(int(input())):
    s=input()
    i=0
    j=len(s)-1
    for k in s:
        if s[j]=="a":
            i+=1
            j-=1
        else:
            print("YES")
            print(s[0:i]+"a"+s[i:])
            break
    else:
        print("NO")

    