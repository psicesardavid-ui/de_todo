class Objeto:
    def __init__(self, nombre = "Manolo", num1 = 0, num2 = 1):
        self.nombre = nombre
        self.num1 = num1
        self.num2 = num2
        
objeto = Objeto()
print(objeto.nombre)

objeto2 = Objeto("Pepe", 5, 3)
print(objeto2.nombre)

objeto2.nombre = "Pepito"
print(objeto2.nombre)

    