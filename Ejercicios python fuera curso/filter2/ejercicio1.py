'''
Ejemplo simple de uso de filtro (filter).
'''

# Genera una lista de números aleatorios entre -10 y 10, crea un filtro 
# que seleccione los números pares positivos y muestra el resultado en pantalla. 

import random


numeros_aleatorios = [random.randint(-10, 10) for _ in range(10)]


numeros_pares_positivos = list(filter(lambda x: x > 0 and x % 2 == 0, numeros_aleatorios))


print("Números aleatorios:", numeros_aleatorios)
print("Números pares positivos:", numeros_pares_positivos)

print("Luis Gálvez Sánchez , 75578608x")
