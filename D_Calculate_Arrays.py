n = int(input())
li = list(map(int,input().split()))
prefix = 0
prefix_arr = []
for elt  in li:
    if elt < 0:
        prefix += elt
        prefix_arr.append(prefix)
        prefix = prefix - elt
    else:
        prefix += elt
        prefix_arr.append(prefix)
print(*prefix_arr)

