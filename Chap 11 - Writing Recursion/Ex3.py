def triangular_numbers(n):
    if n <= 1:
        return 1
    return n + triangular_numbers(n-1)

print(triangular_numbers(7))