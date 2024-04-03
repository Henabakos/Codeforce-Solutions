def can_form_palindrome(n, k, s):
    if k >= n:
        return "NO"

    freq = [0] * 26
    for ch in s:
        freq[ord(ch) - ord('a')] += 1

    odd_count = sum(1 for count in freq if count % 2 != 0)

    if odd_count <= k:
        remaining_chars = n - k
        if remaining_chars % 2 == 0 or (remaining_chars % 2 != 0 and odd_count % 2 != 0):
            return "YES"

    return "NO"


# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read input values for each test case
    n, k = map(int, input().split())
    s = input()

    # Call the function and print the result
    result = can_form_palindrome(n, k, s)
    print(result)