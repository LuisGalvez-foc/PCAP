
import random

nombres=["Kekoñete","elvergalarga","follaViejas","RajoyVuelve","perroSanxe","elvaginazo","RosaMelano","Debora Melo","elPajero"]
clases=["guerrero","mago","clérigo"]

personajes=[{"nombre":random.choice(nombres),"clase":random.choice(clases)} ]

for personaje in personajes:
    print(personaje)