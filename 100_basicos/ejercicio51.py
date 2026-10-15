def calculoFactorial(n):
    if n == 0 or n == 1:
        return 1
    return n * calculoFactorial(n-1)

print(calculoFactorial(3))