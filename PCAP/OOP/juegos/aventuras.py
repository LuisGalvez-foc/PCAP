
class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def esquivar(self):
        import random
        return random.choice([True, False])
    
    def atacar(self, otro_personaje):
        if otro_personaje.vida <= 0:
            raise ValueError(f"{otro_personaje.nombre} ya está derrotado.")
        if not otro_personaje.esquivar():
            otro_personaje.vida -= self.ataque
            return f"{self.nombre} ataca a {otro_personaje.nombre} y causa {self.ataque} de daño."
        else:
            return f"{otro_personaje.nombre} esquiva el ataque de {self.nombre}."
        

class Guerrero(Personaje):
    def __init__(self, nombre, vida, ataque):
        super().__init__(nombre, vida, ataque)
        self.ataque_especial = ataque * 2

    def atacar(self, otro_personaje):
        if otro_personaje.vida <= 0:
            raise ValueError(f"{otro_personaje.nombre} ya está derrotado.")
        if not otro_personaje.esquivar():
            otro_personaje.vida -= self.ataque_especial
            return f"{self.nombre} ataca a {otro_personaje.nombre} con su ataque especial y causa {self.ataque_especial} de daño."
        else:
            return f"{otro_personaje.nombre} esquiva el ataque especial de {self.nombre}."

class Magos(Personaje):
    def __init__(self, nombre, vida, ataque):
        super().__init__(nombre, vida, ataque)
        self.ataque_especial = ataque * 2

    def atacar(self, otro_personaje):
        if otro_personaje.vida <= 0:
            raise ValueError(f"{otro_personaje.nombre} ya está derrotado.")
        if not otro_personaje.esquivar():
            otro_personaje.vida -= self.ataque_especial
            return f"{self.nombre} ataca a {otro_personaje.nombre} con su ataque especial y causa {self.ataque_especial} de daño."
        else:
            return f"{otro_personaje.nombre} esquiva el ataque especial de {self.nombre}."
        

guerrero = Guerrero("Guerrero", 100, 20)
mago = Magos("Mago", 80, 25)



print(guerrero.atacar(mago)) 

print(mago.atacar(guerrero))  

print(guerrero.atacar(mago))
print(mago.atacar(guerrero))
print(guerrero.atacar(mago))
print(mago.atacar(guerrero))
