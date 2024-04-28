
results = []

for _ in range(t):
    s = test_cases[_]

    n = len(s)
    max_area = 0

    for i in range(n):
        consecutive_ones = 0

        for j in range(n):
            width = consecutive_ones + 1
            height = min(i + 1, n - i)
            area = width * height
            max_area = max(max_area, area)

            if j < n - 1 and s[(i + j + 1) % n] == '1':
                consecutive_ones += 1
            else:
                consecutive_ones = 0

    results.append(max_area)

for result in results:
    print(result)