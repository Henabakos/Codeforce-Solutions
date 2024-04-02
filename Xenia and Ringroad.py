n, m = map(int, input().split())
tasks = list(map(int, input().split()))

c = 1  
time = 0

for i in range(m):
    if tasks[i] >= c:
        t = tasks[i] - c
    else:
        t = n - c + tasks[i]

    time += t
    c = tasks[i]

print(time)