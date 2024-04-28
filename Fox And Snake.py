row,col=map(int,input().split())
a=[]
for i in range(51):
    if i%2!=0:
        a.append(i)
        
for i in range(row):
    a1=""
    if i%2==0:
        a1+="#"*col
        print(a1)
    else:
        ind=a.index(i)
        if ind%2==0:
            a1+="."*(col-1)
            a1+="#"
            print(a1)
        else:
            a2="#"
            a1+="."*(col-1)
            a2+=a1
            print(a2)
        