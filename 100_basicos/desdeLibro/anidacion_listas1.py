alien0 = {'color': 'green','points': 5}

alien1 = {'color': 'yellow','points': 10}

alien2 = {'color': 'red','points': 15}

aliens = [alien0, alien1, alien2]

for alien in aliens:
    print(alien)

# print(len(alien))

# hago 30 aliens con ciclo

listaAliens = []

for elemento in range(30):
    algo = {'color': 'indigo','points': 115}
    listaAliens.append(algo)

for alien in listaAliens[:5]:
    print(alien)

print(len(listaAliens))