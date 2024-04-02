def count_greetings(people):
    greetings = 0
    positions = []
    for i in range(len(people)):
        positions.append((people[i][0], 'start'))
        positions.append((people[i][1], 'end'))
    positions.sort()

    current_greetings = 0
    for pos in positions:
        if pos[1] == 'start':
            current_greetings += 1
        else:
            current_greetings -= 1
        greetings += current_greetings

    return greetings



t = int(input())


for _ in range(t):
   
    n = int(input())

    people = []
    for _ in range(n):
        a, b = map(int, input().split())
        people.append((a, b))

    
    result = count_greetings(people)

    
    print(result)