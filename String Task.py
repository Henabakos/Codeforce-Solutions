str1=input()
f=["A","E",'I','O','U',"Y",'a','i','e','o','u','y']
a=''
for i in str1:
    if i not in f:
        a=a+"."+i.lower()
print(a)