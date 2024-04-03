nb=int(input())
boys=list(map(int,input().split()))
ng=int(input())
girls=list(map(int,input().split()))
i,j,cnt=0,0,0
f=min(nb,ng)
boys.sort()
girls.sort()

for k in range(f):
    if boys[i]==girls[j] or boys[i]==(girls[j]+1) or boys[i]+1==girls[j]:
        cnt+=1
        i+=1
        j+=1
    else:
        j+=1
        i+=1
print(cnt)
