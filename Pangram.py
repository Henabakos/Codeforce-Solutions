length_of_str=int(input())
str_=input()
str1=str_.lower()
all_alpha="qwertyuiopasdfghjklzxcvbnm"
for i in all_alpha:
    if i not in str1:
        print("NO")
        break
else:
    print("YES")
