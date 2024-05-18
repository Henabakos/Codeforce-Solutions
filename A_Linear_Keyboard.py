for _ in range(int(input())):
    s=input()
    t=input()
    track={}
    li=[]
    for i in range(len(s)):
        track[s[i]]= i
    
    for i in t:
        li.append(track[i]+1)
    sum1=0
    i,j=0,1
    for k in range(len(li)):
        if j<len(li):
            sum1+=abs((li[j]-li[i]))
            i+=1
            j+=1
        else:
            break
    print(sum1)
        