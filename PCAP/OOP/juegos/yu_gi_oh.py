
class CartaNoEncontradaError(Exception):
    def __init__(self, nombre):
        super().__init__(f'Carta "{nombre}" no encontrada en el mazo.')

class Carta:
    def __init__(self, nombre, ataque, defensa, tipo):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.tipo = tipo

class Jugador:
    def __init__(self):
        self.mazo = []

    def agregar_carta(self, carta):
        self.mazo.append(carta)

    def invocar_carta(self, nombre):
        for carta in self.mazo:
            if carta.nombre == nombre:
                return carta
        raise CartaNoEncontradaError(nombre)
    
    def batalla(self, carta1, carta2):
        print(f"Comienza la batalla entre {carta1.nombre} y {carta2.nombre}!")
        while carta1.defensa > 0 and carta2.defensa > 0:
            print(f"{carta1.nombre} ataca a {carta2.nombre} y causa {carta1.ataque} de daño.")
            carta2.defensa -= carta1.ataque
            if carta2.defensa <= 0:
                print(f"{carta2.nombre} ha sido derrotado!")
                return carta1
            
            print(f"{carta2.nombre} ataca a {carta1.nombre} y causa {carta2.ataque} de daño.")
            carta1.defensa -= carta2.ataque
            if carta1.defensa <= 0:
                print(f"{carta1.nombre} ha sido derrotado!")
                return carta2
            
            print(f"Vida restante: {carta1.nombre}: {max(carta1.defensa, 0)}, {carta2.nombre}: {max(carta2.defensa, 0)}")
        
        if carta1.defensa > carta2.defensa:
            return carta1
        return carta2


"""pruebas"""
jugador1 = Jugador()
jugador2 = Jugador()


carta1 = Carta("Dragón", 100, 2500, "Dragón")
carta2 = Carta("Mago Oscuro", 200, 2100, "Mago")
carta3 = Carta("Guerrero", 1800, 1500, "Guerrero")


jugador1.agregar_carta(carta1)
jugador1.agregar_carta(carta2)
jugador2.agregar_carta(carta3)


try:
    carta_invocada1 = jugador1.invocar_carta("Dragón")
    carta_invocada2 = jugador2.invocar_carta("Guerrero")

    
    ganador = jugador1.batalla(carta_invocada1, carta_invocada2)
    print(f"La carta ganadora es: {ganador.nombre}")
except CartaNoEncontradaError as e:
    print(e)
