class Saiyan:
    Origen="Planeta Vegeta"
    def __init__(self, nombre):
        self.nombre = nombre

class Humano:
    Origen="Tierra"
    def __init__(self, nombre):
        self.nombre = nombre

class Trunks(Humano,Saiyan):
    def __init__(self, nombre,padre,madre):
        super().__init__(nombre)
        self.padre = padre
        self.madre = madre

class Mestizo(Humano, Saiyan):
    def __init__(self, nombre, padre, madre):
        super().__init__(nombre)
        self.padre = padre
        self.madre = madre
    def verAncestros(self):
        for x in Mestizo.__bases__:
            print(x.__name__, end= ' ')
        print()



trunks = Mestizo("Trunks","Vegeta","Bulma")
print(trunks.Origen)  
print(trunks.padre)
print(trunks.madre)
goku=Saiyan("Kakaroto")
vegeta=Saiyan("Veyito")
print(type(goku).__name__)
print(type(vegeta).__name__)
print(trunks.__dict__)


Gohan = Mestizo("Gohan", "Goku", "Chi-Chi")
print(Gohan.nombre)
print(Gohan.padre)
print(Gohan.madre)
print(Gohan.Origen)  

Gohan.verAncestros()

if type(trunks).__name__=="Mestizo":
    if issubclass(Mestizo,Saiyan):
        print("Es Saiyan")
        if issubclass(Mestizo,Humano):
            print("tiene madre huamana")
    else:
        print("No es Saiyan")



print(f"el padre de {trunks.nombre} es {trunks.__dict__["padre"]}")
print(f"la madre de {trunks.nombre} es {trunks.__dict__['madre']}")