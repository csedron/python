def filtrarPalabras(frase, longitudMinima):
    fraseFiltrada = frase.split()
    frase2 = []
    
    for palabra in fraseFiltrada:
        if len(palabra) >= longitudMinima:
            frase2.append(palabra)
    fraseFinal =" ".join(frase2)
    return fraseFinal





# Comprension de listas
# nueva_lista = [ expresión  for elemento in iterable  if condición ]

def filtrarPalabras2(frase, longitudMinima):
    #[palabra for palabra in frase.split() if len(palabra) >= longitudMinima]
    frase1 = [palabra for palabra in frase.split() if len(palabra) >= longitudMinima]
    fraseFinal = " ".join(frase1)
    return fraseFinal

print(filtrarPalabras2('Hola a todos', 4))