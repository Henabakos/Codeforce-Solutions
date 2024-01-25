from math import*
A1,A2,A3=map(int,input().split())
a=int(sqrt((A1*A3)//A2))
b=A1//a
c=A3//a
sum_of_all_edges=4*(a+b+c)
print(sum_of_all_edges)


