menus_las_palmeras = ["Chivito", "Bocadillo de tortilla", "Carne de caballo con ajos"]
menus_el_pirata = ["Bocadillo de calamares", "Bocadillo de melon", "Bocadillo de jamon"]

class Las_palmeras:
    def __init__(self, menus=[]):
        self.menus = menus

class El_pirata:
    def __init__(self, menus=[]):
        self.menus = menus

class Bocadillo:
    def __init__(self, menu):
        self.menu = menu
     
        
def imprime_menu(bocadillo):
    print(f"\nEl bocadillo de {bocadillo.menu} es delicioso!")    
    
def imprime_menus_bar(bar):
    i=0
    print(f"\nLos menús del bar son:")
    for menu in bar.menus:
        print(f"\nMenu {i}: {menu}")    
        i+=1  
        
bar_las_palmeras = Las_palmeras(menus_las_palmeras)
bar_el_pirata = El_pirata(menus_el_pirata)        
bocadillo_cesar = Bocadillo("Bocadillo de huevos revueltos con champiñones")  


imprime_menu(bocadillo_cesar)

print("\n\nMenús de Las Palmeras:")
imprime_menus_bar(bar_las_palmeras)

print("\n\nMenús de El Pirata:")
imprime_menus_bar(bar_el_pirata)

def agregar_menu(bar, menu):
    bar.menus.append(menu)
    

print("\n\nMenús de Las Palmeras después de agregar un nuevo menú:")
agregar_menu(bar_las_palmeras, "Bocadillo de tortilla de patatas\n")

print("\n\nMenús de Las Palmeras:")
imprime_menus_bar(bar_las_palmeras)



   
       
    