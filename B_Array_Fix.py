def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return "NO"
    return "YES"



for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=[]
    e=[]
    for i in l:
        if i>9:
            div=i//10
            mod=i%10
            a.append(div)
            a.append(mod)
        else:
            a.append(i)
    print(is_sorted(a))