num_of_dimasFreinds=int(input())
numOfFingers=list(map(int,input().split()))
sum1=sum(numOfFingers)
a=sum1%(num_of_dimasFreinds+1)
cnt=0
for i in range(sum1+1,sum1+6):
    if i%(num_of_dimasFreinds+1)!=1:
        cnt+=1
    
print(cnt)               
