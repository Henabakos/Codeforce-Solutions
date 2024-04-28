n,t=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
max1=-111111
prefix=[0]
for i in a:
    prefix.append(prefix[-1]+i)
for i in range(n):
    if b[i]==0:
        max1=max(max1,prefix[i])
print(max1)

