import random

def generador_nombres():
    nombres=["Kekoñete","elvergalarga","follaViejas","RajoyVuelve","perroSanxe","elvaginazo","RosaMelano","Debora Melo","elPajero"]
    random.shuffle(nombres)
    for nombre in nombres:
        yield nombre

generador=generador_nombres()


for _ in range(5):
    print(next(generador))