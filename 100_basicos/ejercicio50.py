def concatDicc(d1, d2):
    d1copia = d1.copy() # otra forma
    d1copia.update(d2)
    return d1 | d2 # forma moderna de concatenar

diccionario = {'a': 3, 'b': 6}
diccionario2 = {'c': 2, 'd': -1}
print(concatDicc(diccionario, diccionario2))

