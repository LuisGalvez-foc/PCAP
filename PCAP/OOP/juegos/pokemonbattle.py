
class Pokemon:
    def __init__(self, nombre, tipo, vida, ataque):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.ataque = ataque
        self.tipo_ventaja = self._determinar_tipo_ventaja()

    def _determinar_tipo_ventaja(self):
        tipo_ventaja = {
            "agua": "fuego",
            "fuego": "planta",
            "planta": "agua"
        }
        return tipo_ventaja[self.tipo]
    
    def atacar(self, otro_pokemon):
        if otro_pokemon.vida == 0:
            raise Exception("El otro pokemon ya está debilitado.")
        if self.tipo_ventaja == otro_pokemon.tipo:
            otro_pokemon.vida -= self.ataque * 2
        else:
            otro_pokemon.vida -= self.ataque

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - Vida: {self.vida}"

pokemon1 = Pokemon("Squirtle", "agua", 100, 10)
pokemon2 = Pokemon("Charmander", "fuego", 100, 10)

print(pokemon1)
print(pokemon2)

print("Batalla!")
print(f"{pokemon1.nombre} ataca a {pokemon2.nombre}")
pokemon1.atacar(pokemon2)
print(pokemon2)
print(f"{pokemon2.nombre} ataca a {pokemon1.nombre}")
pokemon2.atacar(pokemon1)
print(pokemon1)

