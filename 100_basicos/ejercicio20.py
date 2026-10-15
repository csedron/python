diccionario = {'Manzana': 3, 'Banana': 7, 'Kiwi': 1}

for fruta in list(diccionario):
    if fruta == 'Kiwi':
        diccionario.pop(fruta)
        #print(fruta)

for clave in diccionario.keys():
    print(clave)
