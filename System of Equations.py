n, m = map(int, input().split())

count = 0

for a in range(int(n**0.5) + 1):
    b = n - a * a
    if a + b * b == m and b >= 0:
        count += 1

print(count)