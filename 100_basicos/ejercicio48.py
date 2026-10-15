def concatListar(L1, L2, L3):
    L4 = []
    for i in L1:
        L4.append(i)
    for i in L2:
            L4.append(i)
    for i in L3:
            L4.append(i)
    return L4

def contarListarMejorada(L1, L2, L3):
    listas = [L1, L2, L3]
    L4 = []
    for elementos in listas:
            for recorro in elementos:
                L4.append(recorro)
    return L4

def contarListarMetodo(L1, L2, L3):
    listas = [L1, L2, L3]
    L4 = []
    for elementos in listas:
            L4.extend(elementos)
    return L4

L1 = [0, 9, 8]
L2 = [2, 6, 9]
L3 = [True, False, 'abc']

L4 = contarListarMetodo(L1, L2, L3)
print(L4)



