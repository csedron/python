personas = {
    'claudio': 'Python',
    'malvina': 'Java',
    'pilar': 'Visual Basic',
    'eva': 'Ada',
    'angela': 'C#',
}

respuesta = input("Ingrese un nombre: ")


if respuesta in personas.keys():
    print(f'Gracias {respuesta} por responder la encuesta')
if respuesta not in personas.keys():
    print(f'{respuesta}, te invito a compltar la encuesta')
        