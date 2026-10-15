def presenciaVocal(frase):
    for i in frase:
        if i in ['a', 'e', 'i', 'o', 'u']:
            return True
    return False
frase = input('Introduzca frase a revisar: ')
print(presenciaVocal(frase))