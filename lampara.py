class Lampara:
    def __init__(self, color, encendida=False):
        self.color = color
        self.encendida = encendida
        
    def encender(self):
        self.encendida = True   
        
    def apagar(self):
        self.encendida = False
        
        
    def cambiar_estado_lampara(lampara):
    
        if lampara.encendida:
            lampara.apagar()
            print("La lámpara está apagada ahora")

        else:
            lampara.encender()
            print("La lámpara está encendida ahora")         
               
                
lampara_01 = Lampara("roja", encendida=True)
lampara_02 = Lampara("verde", encendida=False)

print(f"color de lampara_01: {lampara_01.color}")
print(f"color de lampara_02: {lampara_02.color}")
print(f"¿Esta encendida la lampara_01?: {lampara_01.encendida}")
print(f"¿Esta encendida la lampara_02?: {lampara_02.encendida}")

#cambiar el estado de la lampara_01
Lampara.cambiar_estado_lampara(lampara_01)
print(f"¿Esta encendida la lampara_01: {lampara_01.encendida}") 

#cambiar el estado de la lampara_02
Lampara.cambiar_estado_lampara(lampara_02)  
print(f"¿Esta encendida la lampara_02?: {lampara_02.encendida}")




        
