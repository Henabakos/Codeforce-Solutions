def swap_sort(n, arr):
    swaps = []
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps.append((i, min_idx))
    return swaps



n = int(input())


arr = list(map(int, input().split()))


swaps = swap_sort(n, arr)


print(len(swaps))


for swap in swaps:
    print(swap[0], swap[1])