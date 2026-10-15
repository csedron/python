# L = [3, 2, 6, 9, -1, 5]
L = [-3, -6, 0, 1, 2, 7]

def calcularSuma(L):
    suma = 0
    for i in L:
        suma += i
    return suma

print(calcularSuma(L))
