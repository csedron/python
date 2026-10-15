def posicionEnLista(L, x):
    indices = []
    for posicion, elemento in enumerate(L):
        if elemento == x:
            indices.append(posicion)
          
    if len(indices) == 0:
        print(f'El elemento {x} no esta en la lista {L}')
    return indices 

lista = [6, 8, 9, 1, 3, 7, 6]
posicionEnLista(lista, -1)
print(posicionEnLista(lista, 6))