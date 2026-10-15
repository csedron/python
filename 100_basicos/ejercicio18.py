L = [("Manzana", 15), ("Banana", 8), ("Fresa", 12), ("Kiwi", 9), ("Melocoton", 2)]
""" for fruta, numero in L:
    print(numero) """

# En caso de ordenar por primer elemento
lista = sorted(L)
print(lista)

segundoElemento = sorted(L, key=lambda x: x[1])
print(segundoElemento)