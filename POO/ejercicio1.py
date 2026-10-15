class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print('Estudiando!!!')

estudiante1 = Estudiante('Claudio','50','2 año')

nombre = input('tu nombre: ')
edad = input('tu edad: ')
grado = input('tu grado: ')

estudiante2 = Estudiante(nombre,edad,grado)

estudiar = input()
if (estudiar.lower() == 'estudiar'):
    estudiante2.estudiar()



