def fibonacci(n):
    sequence = []
    if n <= 0:
        return sequence
    elif n == 1:
        sequence.append(0)
        return sequence
    elif n == 2:
        sequence.extend([0, 1])
        return sequence
    else:
        sequence.extend([0, 1])
        for i in range(2, n):
            next_number = sequence[i-1] + sequence[i-2]
            sequence.append(next_number)
        return sequence

# Test the function
number = int(input("Enter the number of Fibonacci numbers to generate: "))
result = fibonacci(number)
print("The Fibonacci sequence is:", result)
