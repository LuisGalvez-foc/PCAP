def potencias_de_2(n):
    potencia=1
    for i in range(n):
        yield potencia
        potencia*=2


for p in potencias_de_2(5):
    print(p)


x = [p for p in potencias_de_2(5)]
print(x)

x=list(potencias_de_2(5))
print(x)