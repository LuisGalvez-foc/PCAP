import random

personajes=[{
    "nombre": "Batman",
    "ataque": random.randint(1, 100)
    }, {
    "nombre": "Superman",
    "ataque": random.randint(1, 100)
    }, {
    "nombre": "boy_tieso",
    "ataque": random.randint(1, 100)
    }, {
    "nombre": "Debora Melo",
    "ataque": random.randint(1, 100)
    }]


print("Ataques antes de incrementar el daño:")
for personaje in personajes:
    print(f"{personaje['nombre']}: {personaje['ataque']}")


ataques = list(map(lambda x: {"nombre": x["nombre"], "ataque": x["ataque"]*1.2 
                              if x["ataque"] > 50 
                              else x["ataque"]}, personajes))


print("Ataques después de incrementar el daño:")
for personaje in ataques:
    print(f"{personaje['nombre']}: {personaje['ataque']}")