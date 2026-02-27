class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        
    def presentarse(self):
        return (f"\nHola, mi nombre es {self.nombre} y mi salario es {self.salario}")
        
        
class Programador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje
        
    def picar_codigo(self):
        return (f"y estoy programando en {self.lenguaje}")
        
        
class Administrador(Empleado):
    def __init__(self, nombre, salario, servidores_a_cargo):
        super().__init__(nombre, salario)
        self.servidores_a_cargo = servidores_a_cargo
        
    def reiniciar_servidor(self):
        return (f"y tengo {self.servidores_a_cargo} servidores a mi cargo que puedo reiniciar\n")
        
        
programador = Programador("Cesar", 10000, "Python")
administrador = Administrador("Maria", 10000, 5)


print(programador.presentarse(), programador.picar_codigo())
print(administrador.presentarse(), administrador.reiniciar_servidor())
