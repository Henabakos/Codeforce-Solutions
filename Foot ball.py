players = input()

dangerous = False
for i in range(len(players) - 6):
    if players[i:i+7] == "0000000" or players[i:i+7] == "1111111":
        dangerous = True
        break

if dangerous:
    print("YES")
else:
    print("NO")