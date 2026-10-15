num = input('Pone un numero: ')

def sumaDigitos(num):
    suma = 0
    for i in str(num):
        suma += int(i)
    return suma

print(sumaDigitos(num))
