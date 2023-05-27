import math

a = int(input("enter range of number to calcultae for fibonacci series"))
b = int(input("enter range of number to calcultae for fibonacci series"))


def is_perfect_square(n):
    root = int(math.sqrt(n))
    return (root * root == n)


def is_fibonacci(n):
    if n == 0:
        return True
    a, b, c = 0, 1, 1
    while c < n:
        a = b
        b = c
        c = a + b
    return c == n or is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)


for i in range(a, b):
    if is_fibonacci(i):
        print(i, "is a Fibonacci number.")
    else:
        print(i, "is not a Fibonacci number.")