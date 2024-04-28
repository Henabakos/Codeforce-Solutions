n=int(input())
s=input()
stack=[0]
for i in s:
    if stack[-1]!=i:
        stack.append(i)
print(n-len(stack)+1)