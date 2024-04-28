from collections import defaultdict
t=int(input())
li=list(map(int,input().split()))
s=input()
stack=[]
container=defaultdict(int)
for i,key in enumerate(li):
    container[key]=i

li.sort()
i=0
for j in s:
    if j=="0":
        print(container[li[i]]+1,end=" ")
        stack.append(container[li[i]]+1)
        i+=1
    else:
        print(stack.pop(),end=" ")
