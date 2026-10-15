def calculoMCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(calculoMCD(15, 3))