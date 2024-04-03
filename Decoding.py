from collections import deque
n=int(input())
str1=input()
deq=deque()

if len(str1) % 2!=0:
    for i in range(len(str1)):
        if i%2!=0:
            deq.appendleft(str1[i])
        else:
            deq.append(str1[i])
else:
    for i in range(len(str1)):
        if i%2!=0:
            deq.append(str1[i])
        else:
            deq.appendleft(str1[i])
        
print("".join(deq))