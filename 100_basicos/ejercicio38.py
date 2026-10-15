L = [0, 3, 5, 7, 3, 5, 1, -1]

def eliminarDuplicados(L):
    ordenada1 = set(L)
    ordenada = list(sorted(ordenada1, reverse=False))
    return ordenada

print(eliminarDuplicados(L))
