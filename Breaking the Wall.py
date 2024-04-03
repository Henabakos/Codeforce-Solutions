def minimum_onager_shots(n, durability):
    min_shots = float('inf')

    for i in range(n):
        shots = 0

        # Calculate shots needed to break section i
        if i > 0:
            shots += max(0, durability[i] - durability[i - 1] + 1)
        if i < n - 1:
            shots += max(0, durability[i] - durability[i + 1] + 1)

        min_shots = min(min_shots, shots)

    return min_shots


# Read the number of sections
n = int(input())

# Read the durability of sections
durability = list(map(int, input().split()))

# Call the function to calculate the minimum number of onager shots
result = minimum_onager_shots(n, durability)

# Print the result
print(result)