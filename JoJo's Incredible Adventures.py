def maximum_rectangle_area(t, test_cases):
    results = []

    for _ in range(t):
        s = test_cases[_]

        # Find the maximum area of a rectangle consisting only of ones
        n = len(s)
        max_area = 0

        # Iterate through each row of the table
        for i in range(n):
            consecutive_ones = 0

            # Iterate through each column of the table
            for j in range(n):
                # Calculate the width of the rectangle
                width = consecutive_ones + 1

                # Calculate the height of the rectangle
                height = min(i + 1, n - i)

                # Calculate the area of the rectangle
                area = width * height

                # Update the maximum area if necessary
                max_area = max(max_area, area)

                # Check if the next column has a one
                if j < n - 1 and s[(i + j + 1) % n] == '1':
                    consecutive_ones += 1
                else:
                    consecutive_ones = 0

        results.append(max_area)

    return results


# Read the number of test cases
t = int(input())

# Read the test cases
test_cases = []
for _ in range(t):
    s = input().strip()
    test_cases.append(s)

# Call the function to calculate the maximum rectangle areas
results = maximum_rectangle_area(t, test_cases)

# Print the results
for result in results:
    print(result)