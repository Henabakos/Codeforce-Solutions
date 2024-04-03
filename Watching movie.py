from collections import Counter
a="Timur"
t=int(input())
for i in range(t):
    n=int(input())
    name=input()
    cnt=Counter(name)
    cnt2=Counter(a)
    if cnt==cnt2:
        print("YES")
    else:
        print("NO")

    