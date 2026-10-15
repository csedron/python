def controlMay(frase):
    contador = 0
    for i in frase:
        if i.isupper():
            contador +=1
    if contador >=1:
        return True
    else:
        return False


def controlMayMejorada(frase):
    for i in frase:
        if i.isupper():
            return True
        else:
            return False

frase = 'Estoy aprendiendo'
resultado = controlMayMejorada(frase)
print(resultado)