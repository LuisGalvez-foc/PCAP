mi_lista=[]

for x in range(11):
    mi_lista.append(1 if x % 2 == 0 else 0)

print(mi_lista)


mi_lista=[1 if x % 2 == 0 else 0 for x in range(11)]


print(mi_lista)