# n=int(input())
# li=list(map(int,input().split()))
# i,j,f=0,len(li)-1,len(li)-1

# while(j>i):
#     if li[i]<=li[j]:
#         i+=1
#     else:
#         j-=1
# print(i+1,f-j)
i = 0
j = 0
cnt1 = 0
cnt2 = 0

n = int(input())
li = list(map(int,input().split()))
while len(li) > 0:
    if j != 0:
        j -= 1
    if cnt2 != 0:
        cnt2 -= 1
    if j == 0:
        j = li[0]
        i += 1
        li.pop(0)
    if cnt2 == 0:
        if len(li) == 0:
            break
        else:
            cnt2 = li[-1]
            cnt1 += 1
            li.pop()

print(i, cnt1)
