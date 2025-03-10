'''
La función filter() comprueba que los elementos de una serie (ej. una lista) cumplen una condición, 
y devuelve un iterador compuesto por tales elementos.
'''

lista_numerica = [17, -24, 7, 40, -23, 51, 70, 82, -96, 102]
print("Lista de números: ", lista_numerica)

# A partir de la lista de números, crea un filtro que seleccione los números pares, 
# y muestra el resultado en pantalla. 

filtro_pares = filter(lambda x: x % 2 == 0, lista_numerica)
print("Lista de números pares: ", list(filtro_pares))


# A partir de la lista de números, crea un filtro que seleccione los números pares > 0, 
# y muestra el resultado en pantalla. 

filtro_pares_positivos = filter(lambda x: x % 2 == 0 and x > 0, lista_numerica)
print("Lista de números pares positivos: ", list(filtro_pares_positivos))

print("Luis Gálvez Sánchez , 75578608x")



