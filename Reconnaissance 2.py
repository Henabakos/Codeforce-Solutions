n=int(input())
soldier_height=list(map(int,input().split()))
mindef=10000
for i in range(len(soldier_height)):
    if i+1 <=len(soldier_height)-1:
        a=abs(soldier_height[i]-soldier_height[i+1])
        if a<mindef:
            c,d=i,i+1
        mindef=min(a,mindef)
    else:
        a=abs(soldier_height[i]-soldier_height[0])
        if a<mindef:
            c,d=i,0
        mindef=min(a,mindef)

print(c+1,d+1)

            