class Persona:
    def __init__(self,nombre ,edad ,dni ,peso ,piel):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.peso = peso
        self.piel = piel



    def __str__(self):
        return "Nombre : {} \nEdad : {} \nDNI : {} \nPeso : {} \nColor de piel : {}".format(self.nombre,self.edad,self.dni,self.peso,self.piel)

    def mayor_edad(self):
        if self.edad >= 18 :
            print(self.nombre + " es mayor de edad")
        else:
            print(self.nombre + " es menor de edad")

    def color(self):
        if self.piel == "morena":
            print(self.nombre + " es moreno")
        else:
            print(self.nombre + " es blanco")
print("=======PERSONA========")
persona1 = Persona("carlos",21,12312121,"18Kg","blanca")
print(persona1)
persona1.mayor_edad()
persona1.color()
print("======================")
