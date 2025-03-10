class Item:
    def __init__(self, nombre, tipo, rareza):
        self.nombre = nombre
        self.tipo = tipo
        self.rareza = rareza

class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = []
        self.max_inventario = 5
        self.inventario_lleno = False
       
    def agregar_item(self, item):
        if len(self.inventario) < self.max_inventario:
            self.inventario.append(item)
        else:
            self.inventario_lleno = True
            print("Inventario lleno")


    def eliminar_item(self, item):
        if item in self.inventario:
            self.inventario.remove(item)
        else:
            print("El objeto no está en el inventario")
    
    def mostrar_inventario(self):
        if self.inventario_lleno:
            print("El inventario está lleno")
        else:
            print("Inventario del personaje:", self.nombre)
            for item in self.inventario:
                print(item.nombre, item.tipo, item.rareza)

"""prueba"""
personaje = Personaje("kekoñete")

item1 = Item("espada", "arma", "común")
item2 = Item("escudo", "defensa", "raro")
item3 = Item("pocion", "pocion", "común")
item4 = Item("amuleto", "accesorio", "legendario")
item5 = Item("casco", "defensa", "raro")

personaje.agregar_item(item1)
personaje.agregar_item(item2)
personaje.agregar_item(item3)
personaje.agregar_item(item4)
personaje.agregar_item(item5)

"""prueba de inventario lleno"""
personaje.agregar_item(item1)

personaje.mostrar_inventario()

personaje.eliminar_item(item2)

personaje.mostrar_inventario()

