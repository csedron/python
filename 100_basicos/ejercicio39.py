def anadirElementoDicc(clave,valor,d):
    d[clave] = valor
    print(d)
    return d

anadirElementoDicc('baptiste', 29, {'julien': 14, 'laurent': 31})
anadirElementoDicc('peso', 65.3, {})