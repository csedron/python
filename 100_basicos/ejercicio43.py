def minimo(L):
    num = float('inf')
    for a in L:
        if a < num:
            num = a
    return num

L = [-9, 2, 4, 1, 8]
L = [-3, 1, 7, 6, 2, 3]
print(minimo(L))