import time

# Inicio de medicion
inicio = time.perf_counter()

# Lo que queremos medir
for i in range(0,11):
   total = 8 * i
   print(f'8 x {i} ' + '= ' + str(total))

# Fin de medicion
fin = time.perf_counter()
total = fin - inicio
print(f'El script tardo en ejecutarse {total:.6f} segundos')