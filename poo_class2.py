class Auto:
    def __init__(self,marca ,modelo , capacidad,tipo,estado):
        self.marca = marca
        self.modelo = modelo
        self.capacidad = 11
        self.tipo = tipo
        self.estado = estado

    def __str__(self):
        return "Marca : {} \nModelo : {} \nAsientos ocupados : {} \nCombustible : {} \nestado : {}".format(self.marca,self.modelo,self.capacidad,self.tipo,self.estado)

    def posicion(self):
        if self.estado == 1:
            print("El automovil esta encendido")
        else:
            print("El automovil esta apagado")

    def tamaño(self):
        if self.capacidad >= 11:
            print("el automovil esta lleno")
        else:
            print("el automovil tiene espacio")

print("=========AUTOMOVIL==========")
car = Auto("Toyota",1996,4,"Gas",0)
print(car)
car.posicion()
car.tamaño()
print("=============================")