import random
import time

class Dragon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = random.randint(80, 120)
        self.fuerzaBase = random.randint(15, 25)

    def atacar(self, oponente):
        daño = random.randint(self.fuerzaBase - 5, self.fuerzaBase + 5)
        oponente.vida -= daño
        print(f"\n{self.nombre} lanza un ataque feroz!")
        print(f"{oponente.nombre} recibe {daño} de daño. HP: {max(0, oponente.vida)}")
        time.sleep(1)
        
num_dragones = 80
luchadores = []

for i in range(num_dragones):
    luchadores.append (Dragon(f"dragón{i}"))
    print(len(luchadores))
    
luchadores[70].vida = 0

for luchador in luchadores:
    if luchador.vida == 0:
        muertito = luchador
        print(muertito.nombre, muertito.vida)
        
def quita_al_muerto():
    for luchador in luchadores:
        if luchador.nombre == muertito.nombre:
            luchadores.remove(luchador)
            
quita_al_muerto()

print(len(luchadores))

    
    