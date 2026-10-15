def mediaLista(L):
    contador = 0
    sumatoria = 0
    for a in L:
        contador += 1
        sumatoria +=a
    return sumatoria / contador

L = [1, 2, 3, 4, 5, 6, 7]
L = [3, 0, -1, 5, 6, 9, 17]

print(mediaLista(L))
