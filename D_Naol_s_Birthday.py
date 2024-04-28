
s = input().strip()

stack = []
mini = s[n-1]
mind = [0] * n
mind[n-1] = n-1

for i in range(n-2, -1, -1):
    mind[i] = mind[i+1]
    if s[i] <= mini:
        mini = s[i]
        mind[i] = i

m = 0
final = ""

while m < n:
    if not stack:
        stack.append(m)
        m += 1
        continue

    while m < n and stack[-1] < mind[stack[-1]]:
        stack.append(m)
        m += 1

    if stack[-1] == mind[stack[-1]]:
        final += s[stack[-1]]
        stack.pop()

        if not stack:
            continue

        if s[mind[m]] < s[stack[-1]]:
            mind[stack[-1]] = mind[m]
        else:
            mind[stack[-1]] = stack[-1]

while stack:
    final += s[stack[-1]]
    stack.pop()

print(final)