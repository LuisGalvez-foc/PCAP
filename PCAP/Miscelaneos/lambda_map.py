lista_nuemrica=[x for x in range(5)]


lista_cuadrados= list(map(lambda x:x**2,lista_nuemrica))
print(lista_cuadrados)


for x in map (lambda x:x**2,lista_cuadrados):
    print(x,end=" ")
print()