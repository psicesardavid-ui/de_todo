class Jugute:
    def __init__(self, nombre, color, tamano):
        self.nombre = nombre
        self.color = color
        self.tamano = tamano

juguete_01 = Jugute("Coche", "Rojo", "L")
juguete_02 = Jugute("Pelota", "Amarillo", "XL")
juguete_03 = Jugute("Cohete", "Verde", "M")
juguete_04 = Jugute("Pelota", "Rosa", "S")

jugueteria = [juguete_01, juguete_02, juguete_03, juguete_04]


busco = "Pelota"
reemplazar = "Balon"

def reemplazar_nombre(busco, reemplazar, donde):
    for item in donde:
        if item.nombre == busco:
            item.nombre = reemplazar
            
reemplazar_nombre("Pelota", "Balon", jugueteria)

#print(jugueteria[1].nombre)

for juguete in jugueteria:
    print(f"\nJuguete: {juguete.nombre} \nColor: {juguete.color} \nTamaño: {juguete.tamano}\n")

