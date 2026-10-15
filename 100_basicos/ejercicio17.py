L1 = [9, 8, 7, 14, 3, 2, "a", "p", "hola", "b"]
L2 = ["b", 1, 9.2, 6, 3, 9, "p"]

#interseccion de dos listas usando para esto "set"
print('interseccion de dos listas usando para esto "set"')
l3 = list(set(L1) & set(L2))
print(l3)

# usando comprension de listas
# variable = [expresion for elemento in iterable if condicion]
L4 = [elemento for elemento in L1 if elemento in L2]
print('interseecion de listsas por comprension de listas')
print(L4)