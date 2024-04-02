coin_num=int(input())
value_of_coins=list(map(int,input().split()))
value_of_coins.sort()
sum_of_the_coins=sum(value_of_coins)//2
sum_list=[]
total,cnt=0,0

for i in value_of_coins:
    total+=i
    sum_list.append(total)

for i in range(coin_num):
    if sum_list[i]<=sum_of_the_coins:
        cnt+=1
print(cnt)
