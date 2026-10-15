# variable = [expresion for elemento in iterable if condicion]
def sumaSublista(L, i, j):
    suma = 0
    for a in L[i:j+1]:
        suma += a
    return suma

L = [4, 10, 12, 16, 18]
L = [2, 4, 6, 8, 10, 12 ]
print(sumaSublista(L, 0, 2))