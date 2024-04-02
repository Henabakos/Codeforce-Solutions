num=int(input())
str1=input()
li=[]
for i in range(1,num+1):
    if num%i==0:
        li.append(i)
for i in li:
    str1=str1[i-1::-1]+str1[i:]
print(str1)



