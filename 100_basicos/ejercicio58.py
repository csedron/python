def numeroOcurrencias(L):
    lista = []
    listaAuxiliar = []
    for conteo in L:
        if conteo not in listaAuxiliar:
            listaAuxiliar.append(conteo)
            cuento1 = L.count(conteo)
            lista.append((conteo,cuento1))
    print(lista)

L = [-4, 8, -3, 2, 1, 2, 7, 9, -3, 8, 1]
numeroOcurrencias(L)