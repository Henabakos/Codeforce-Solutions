from collections import Counter
t=int(input())
s=input()

a=Counter(s)
f=t//4

new=""
li=[]
if len(a)<4:
    print("===")
else:
    for i in range(len(s)):
        if a[s[i]]!=f and s[i]!='?':
            li.append(s[i])
    i,j=0,0
    for k in range(len(s)):
        if s[k]=="?":
            new+=li[j]
            j+=1
        else:
            new+=s[k]
    print(new)
      

            


