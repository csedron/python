a = int(input("pone un numero a verificar: "))
L = [-6, 5, -3, -1, 2, 8, -3.6]

def verifPresencia(a, L):
    if a in L:
        print(True)
    else:
        print(False)

verifPresencia(a, L)