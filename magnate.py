t=int(input())
a=[]
for i in range(t):
    s=input()
    a.append(s)
cnt=1
for i in range(t):
    if i<=len(a)-2:
        if a[i]!=a[i+1]:
            cnt+=1
            
print(cnt)
    
