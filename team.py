t=int(input())
cnt=0
for i in range(t):
    li=list(map(int,input().split()))
    if li.count(1)>=2:
        cnt+=1
print(cnt)