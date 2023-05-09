class Persona:
    def __init__(self, nombre, edad, masa, DNI, pais):
        self.nombre = nombre
        self.edad = edad
        self.masa = masa
        self.DNI = DNI
        self.pais= pais

        
nombre = input("Ingresa el nombre de la persona: ")
edad = int(input("Ingresa la edad de la persona: "))
peso = int(input("Ingresa la masa de la persona(en kg)")) 
DNI =  int(input("Ingresa el DNI (Documento de identidad) de la persona"))
pais = input("Ingresa el pais de la persona: ")

persona = Persona(nombre, edad, masa, DNI, pais)

print("Nombre:", persona.nombre)
print("Edad:", persona.edad)
print("Masa:", persona.masa)
print("DNI:", persona.DNI)    
print("Pais:", persona.pais)