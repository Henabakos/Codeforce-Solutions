length = int(input())

s = input()
t = input()

counter = 0
flagA = False
flagB = False


if s.count("1") != t.count("1"):
    print(-1)
else:
    for i in range(length):
       if int(s[i]) - int(t[i]) == 0 and (flagA == True or flagB == True):
           break
       elif int(s[i]) - int(t[i]) == 1:
           if flagB == True:
               break
           counter += 1
           flagA = True
       elif int(s[i]) - int(t[i]) == -1:
           if flagA == True:
               break
           counter += 1
           flagB = True
    print(counter)
               