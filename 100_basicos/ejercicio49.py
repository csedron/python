def numValoresDicc(d):
    contador = 0
    for i in d.values() :
        for a in i:
            contador += 1
    return contador
        
        
diccionario = {'a': [1, 2, 3], 'b': [3, 'p'], 'c': [8]}
print(numValoresDicc(diccionario))
