import random

class PersonajeGacha:
    def __init__(self, nombre, rareza, elemento):
        self.nombre = nombre
        self.rareza = rareza
        self.elemento = elemento
        self.__id_secreto = self.__generar_id_secreto()

    def __generar_id_secreto(self):
        letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digitos = '0123456789'
        id_secreto = ''.join(random.choice(letras) for i in range(2))
        id_secreto += ''.join(random.choice(digitos) for i in range(3))
        return id_secreto


pokemons = [
    PersonajeGacha("Pikachu", 5, "Eléctrico"),
    PersonajeGacha("Charizard", 4, "Fuego"),
    PersonajeGacha("Bulbasaur", 3, "Planta"),
    PersonajeGacha("Squirtle", 3, "Agua"),
    PersonajeGacha("Jigglypuff", 4, "Normal"),
    PersonajeGacha("Gengar", 5, "Fantasma"),
    PersonajeGacha("Eevee", 3, "Normal"),
    PersonajeGacha("Snorlax", 4, "Normal"),
    PersonajeGacha("Mewtwo", 5, "Psíquico"),
    PersonajeGacha("Lapras", 4, "Hielo"),
    PersonajeGacha("Dragonite", 5, "Dragón"),
    PersonajeGacha("Alakazam", 4, "Psíquico"),
    PersonajeGacha("Machamp", 3, "Lucha"),
    PersonajeGacha("Gyarados", 4, "Agua"),
    PersonajeGacha("Arcanine", 4, "Fuego"),
    PersonajeGacha("Vaporeon", 4, "Agua"),
    PersonajeGacha("Jolteon", 4, "Eléctrico"),
    PersonajeGacha("Flareon", 4, "Fuego"),
    PersonajeGacha("Umbreon", 4, "Siniestro"),
    PersonajeGacha("Espeon", 4, "Psíquico"),
    PersonajeGacha("Blastoise", 4, "Agua"),
    PersonajeGacha("Venusaur", 4, "Planta"),
    PersonajeGacha("Rhydon", 3, "Roca"),
    PersonajeGacha("Nidoking", 3, "Veneno"),
    PersonajeGacha("Clefable", 3, "Hada"),
    PersonajeGacha("Ninetales", 4, "Fuego"),
    PersonajeGacha("Exeggutor", 4, "Planta"),
    PersonajeGacha("Starmie", 4, "Agua"),
    PersonajeGacha("Scyther", 4, "Bicho"),
    PersonajeGacha("Electabuzz", 4, "Eléctrico"),
    PersonajeGacha("Magmar", 4, "Fuego"),
    PersonajeGacha("Pinsir", 4, "Bicho"),
    PersonajeGacha("Tauros", 4, "Normal"),
    PersonajeGacha("Gyarados", 4, "Agua/Volador"),
    PersonajeGacha("Lapras", 4, "Agua/Hielo"),
    PersonajeGacha("Ditto", 3, "Normal"),
    PersonajeGacha("Eevee", 3, "Normal"),
    PersonajeGacha("Porygon", 3, "Normal"),
    PersonajeGacha("Omastar", 4, "Roca/Agua"),
    PersonajeGacha("Kabutops", 4, "Roca/Agua"),
    PersonajeGacha("Aerodactyl", 4, "Roca/Volador"),
    PersonajeGacha("Snorlax", 4, "Normal"),
    PersonajeGacha("Articuno", 5, "Hielo/Volador"),
    PersonajeGacha("Zapdos", 5, "Eléctrico/Volador"),
    PersonajeGacha("Moltres", 5, "Fuego/Volador"),
    PersonajeGacha("Dratini", 3, "Dragón"),
    PersonajeGacha("Dragonair", 4, "Dragón"),
    PersonajeGacha("Dragonite", 5, "Dragón/Volador"),
    PersonajeGacha("Mew", 5, "Psíquico")
]


def invocar_pokemon():
    while True:
        pokemon = random.choice(pokemons)
        if pokemon.rareza == 5 and random.random() < 0.05:
            return pokemon
        elif pokemon.rareza == 4 and random.random() < 0.15:
            return pokemon
        elif pokemon.rareza == 3 and random.random() < 0.8:
            return pokemon

pokemon_invocado = invocar_pokemon()
print(f"¡Has invocado a {pokemon_invocado.nombre} de rareza {pokemon_invocado.rareza} y elemento {pokemon_invocado.elemento}!")