for _ in range(int(input())):
    _set=set()
    li=[]
    n=int(input())
    for i in range(n):
        li.append(input())
        _set.add(li[i])
    res=[]
    for k in range(n):
        j=0
        while(j<len(li[k])):
            if li[k][:j+1] in _set and li[k][j+1:] in _set:
                res.append("1")
                break
            j+=1
        else:
            res.append("0")
    print("".join(res))
