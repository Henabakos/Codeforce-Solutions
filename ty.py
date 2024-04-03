
# t=int(input())
# for _ in range(t):
#     n=int(input())
#     sum1=0
#     li=list(map(int,input().split()))
#     li.sort(reverse=True)
#     for i in li:
#         if i<0:
#             sum1+=abs(i)
#         else:
#             sum1+=i
#     print(sum1)
# n,m=map(int,input().split())
# a=list(map(int,input().split()))

# pos=1
# time=0
# for i in a:
#     if i>=pos:
#         t=i-pos
#     else:
#         t=n-pos+i
    
#     time+=t
#     pos=i
# print(time)
# n=int(input())
# li=list(map(int,input().split()))
# hh=sum(li)
# m=int(input())
# all=[]
# for _ in range(m):
#     a,b=map(int,input().split())
#     for i in range(a,b+1):
#         all.append(i)
# if hh<=len(all):
#     print(hh)
# else:
#     print("-1")
# n=int(input())
# li=list(map(int,input().split()))
# i,j=0,1
# while(li[i]!=0):
#     for k in range(n):
#         li[k]-=1

#     if i==n-1:
#         i=0
#     else:
#         i+=1
# print(i+1)
t=int(input())
for _ in range(t):
    n=int(input())
    str1=input()
    if "B" and "R" in str1 and "W" not in str1:
        print("YES")
    elif "B" and "R" in str1:
        for i in range(len(str1)):
            if str1[i]=="W":
                if "B" not in str1[i:] and "R" not in str1[i:]:
                    print("YES")
                    break
                else:
                    print("NO")
                    break
    
        

        

        


