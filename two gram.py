t=input()
cnt={}
b=0
for i in range(len(t)):
    a=t[i:i+2]
    if a in cnt:
        cnt[a]+=1
    else:
        cnt[a]=1
for i in cnt.values():
    b=max(b,i)

for key,value in cnt.items():
    if value==b:
        print(key)
        break