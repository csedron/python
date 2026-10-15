def invertirFrase(frase):
    frase1 = [palabra for palabra in frase.split(" ") if palabra]
    frase2 = []
    for palabra in reversed(frase1):
        frase2.append(palabra)
    final = " ".join(frase2)
    return final

def invertirFrase2(frase):
    fraseInvertida = [palabra for palabra in frase.split(" ")]
    return " ".join(reversed(fraseInvertida))

print(invertirFrase2("Me parece que te agarro"))