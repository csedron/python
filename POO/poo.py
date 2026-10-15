class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    # Metodos de Objetos

    def llamar(self):
        print(f'Estas llamando desde tu: {self.modelo}')

    def mandar(self):
        print(f'Enviando mensajes desde tu: {self.modelo}')

celular2 = Celular('Xiaomi', 'T70', '120Mpx')
celular3 = Celular('Apple', '18 Pro Max', '200Mpx')
print(celular2.modelo)
celular2.llamar()
celular3.mandar()