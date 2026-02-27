class vehiculo:
    def __init__(self, chasis, motor, ruedas, color):
        self.chasis = chasis
        self.motor = motor   
        self.ruedas = ruedas
        self.color = color
        
        
class coche(vehiculo):
    def __init__(self, chasis, motor, ruedas, color, aire, puertas, direccion_hidraulica, carroceria):
        super().__init__(chasis, motor, ruedas, color)
        self.aire = aire
        self.puertas = puertas
        self.direccion_hidraulica = direccion_hidraulica
        self.carroceria = carroceria
        
    def mostrar_informacion_coche(self):
        print(f"\nCoche:")
        print(f"Chasis: {self.chasis}")
        print(f"Motor: {self.motor}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Color: {self.color}")
        print(f"Aire acondicionado: {self.aire}")
        print(f"Puertas: {self.puertas}")
        print(f"Dirección hidráulica: {self.direccion_hidraulica}")
        print(f"Carrocería: {self.carroceria}")
        
        
class moto(vehiculo): 
    def __init__(self, chasis, motor, ruedas, color, pata_cabra, pedales, manubrio):
        super().__init__(chasis, motor, ruedas, color)
        self.pata_cabra = pata_cabra
        self.pedales = pedales
        self.manubrio = manubrio
        
    def mostrar_informacion_moto(self):
        print(f"\nMoto:")
        print(f"Chasis: {self.chasis}")
        print(f"Motor: {self.motor}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Color: {self.color}")
        print(f"Pata de cabra: {self.pata_cabra}")
        print(f"Pedales: {self.pedales}")
        print(f"Manubrio: {self.manubrio}\n")
        
        
#casos de uso
coche_01 = coche("chasis_01", "motor_01", 4, "rojo", True, 4, True, "sedan")
moto_01 = moto("chasis_02", "motor_02", 2, "negro", True, True, True)

coche_01.mostrar_informacion_coche()
moto_01.mostrar_informacion_moto()