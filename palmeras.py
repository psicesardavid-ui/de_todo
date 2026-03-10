class Las_palmeras:
    def __init__(self, menus=[]):
        self.menus = menus
        

class Bocadillo (Las_palmeras):
    def __init__(self, menu=[]):
        super().__init__(menus)
        self.menu = menu
        

menus = ["chivito", "brascada", "calamares", "almusafes", "vegetal", "atun con olivas", "carne de caballo con ajos", "el de la casa", "rojo y negro"]
las_palmeras = Las_palmeras(menus)


i=0
for menu in las_palmeras.menus:
    print(f"menu {i} {menu}")
    i+=1
    

bocadillo_guille = Bocadillo(las_palmeras.menus[1])
bocadillo_prisca = Bocadillo(las_palmeras.menus[6])
print(f"\nEl bocadillo de Guille es {bocadillo_guille.menu}")
print(f"El bocadillo de Prisca es {bocadillo_prisca.menu}")