n,m = map(int,input().split())
li=list(map(int,input().split()))
li.sort()
cnt = 0
for i in range(m):
    if li[i] < 0:
        cnt += abs(li[i])
print(cnt)