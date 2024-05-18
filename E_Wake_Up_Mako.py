n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
total,prefix=0,[]
_max=0
ind_0=[]
for i in a:
    total+=i
    prefix.append(total)
for ind,value in enumerate(b):
    if value==0:
        ind_0.append(ind)

i,j=0,k-1
while(j<len(ind_0)):
    _max=max(_max,prefix[ind_0[j]]-prefix[ind_0[i]-1])
    j+=1
    i+=1
print(_max)
    