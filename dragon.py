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
    luchadores.append(f"Dragón (i+1)")
    
print(len(luchadores))

luchadores[70].vida = 0

for luchador in luchadores:
    if luchador.vida == 0:
        muertito = luchador
        
        


def quita_al_muerto():
    for luchador in luchadores:
        if luchador.nombre == muertito.nombre:
            luchadores.remove(luchador)

    
    
dragon_1 = Dragon("Smaug")
dragon_2 = Dragon("Drogon")
dragon_3 = Dragon("Fafnir")
dragon_4 = Dragon("Viserion")

luchadores = [dragon_1, dragon_2, dragon_3, dragon_4]
random.shuffle(luchadores)

atacante_inicial = luchadores[0]
segundo_atacante = luchadores[1]
tercer_atacante = luchadores[2]
cuarto_atacante = luchadores[3]



print("--- ¡COMIENZA LA BATALLA! ---")
print(f"{atacante_inicial.nombre} tiene la iniciativa y ataca primero.")
    
while atacante_inicial.vida > 0 and segundo_atacante.vida > 0:
    atacante_inicial.atacar(segundo_atacante)

    if segundo_atacante.vida > 0:
        segundo_atacante.atacar(atacante_inicial)

ganador = atacante_inicial if atacante_inicial.vida > 0 else segundo_atacante

print(f"\n" + "="*30)
print(f"¡EL VENCEDOR ES {ganador.nombre.upper()}!")
print(f"Vida restante: {ganador.vida}")
print("="*30)

