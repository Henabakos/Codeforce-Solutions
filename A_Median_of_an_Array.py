
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    p = (n + 1) // 2 - 1
    res = a[p:].count(a[p])
    print(res)

t = int(input())

for _ in range(t):
    solve()
