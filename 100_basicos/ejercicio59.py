def unionLista(L1, L2, L3):
    listaAuxiliar = []
    for elemento in L1 + L2 + L3:
        if elemento not in listaAuxiliar:
            listaAuxiliar.append(elemento)
    print(listaAuxiliar)
    listaAuxiliar.sort()
    final = ",".join(map(str, listaAuxiliar))
    print(final)
unionLista([3,6,9,3], [1,0,3], [12,6,0])
