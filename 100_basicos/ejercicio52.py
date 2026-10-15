def divisoresMult(n, a, numUmbral):
    lista = []
    for i in range(0, numUmbral+1):
        if (i % n == 0) and (i % a != 0):
            lista.append(i)
    return lista

print(divisoresMult(11, 3, 85))
print(divisoresMult(5, 2, 100))
