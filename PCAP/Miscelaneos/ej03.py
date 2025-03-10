import random

nombres=["Cr7","Messi","Luizao","boy_tieso","Debera Melo","Belen esteban","Montoya","chicote", "Pequeño Nicolás","Terelu Campos"]
clases=["guerrero","mago","clérigo"]

personajes=[{
            "nombre":random.choice(nombres),
            "clase":random.choice(clases),
            "nivel":random.randint(1, 10)}for i in range(5)] 
            
personajes_nivel_alto = filter(lambda x: x["nivel"] > 5, personajes)
for personaje in personajes_nivel_alto:
    print(personaje)