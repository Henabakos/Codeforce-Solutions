def untangle_wires(sequence):
    stack = []

    for char in sequence:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    if stack:
        return "No"
    else:
        return "Yes"



sequence = input().strip()


result = untangle_wires(sequence)


print(result)