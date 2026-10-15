def maximo(L):
    minimo_absoluto = float('-inf')
    for i in L:
        if i > minimo_absoluto:
            minimo_absoluto = i
    print(minimo_absoluto)

lista = [-9, 2, 4, 1, 8]
lista = [-3, 1, 7, 6, 2, 3]
maximo(lista)