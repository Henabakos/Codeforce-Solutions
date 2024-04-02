t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    cnt=a
    while(b%3!=0):
        b+=1
        c-=1
    if c<0:
        print(-1)
        continue
    else:
        r=c//3
        v=c%3
        if v==0:
            print(cnt+(b//3)+r)
        else:
            print(cnt+(b//3)+r+1)
            

       
    
   

