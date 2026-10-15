def eliminarEsp(frase):
    fraseFinal = ''
    for i in frase:
        if i != ' ':
            fraseFinal += i
    print(fraseFinal)

eliminarEsp('basico Base')