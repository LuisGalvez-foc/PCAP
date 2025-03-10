class Reptil:
    def __init__(self, nombre):
        self.nombre = nombre

class Serpiente(Reptil):
    pass


class Culebra(Serpiente):
    pass




reptil1=Reptil("lagarto")
reptil2=Serpiente("Mamba negra")
reptil3=Culebra("culebra iberica")

print("--------------------------------------")

print(Reptil.__name__)
print(Serpiente.__name__)
print(Culebra.__name__)

print("--------------------------------------")

print(type(reptil1).__name__)
print(type(reptil2).__name__)
print(type(reptil3).__name__)

print("--------------------------------------")

print(f"\t     {Reptil.__name__}    {Serpiente.__name__}   {Culebra.__name__}")

for reptil1 in [Reptil,Serpiente,Culebra]:
    print(reptil1.__name__,end="  \t")  
    for reptil2 in [Reptil,Serpiente,Culebra]:
        print(issubclass(reptil1,reptil2),end ="\t")
    print()

print("--------------------------------------")

for reptil1 in [Reptil,Serpiente,Culebra]:
    print(reptil1.__name__,end="  \t")  
    for reptil2 in [Reptil,Serpiente,Culebra]:
        print(issubclass(reptil1,reptil2),end ="\t")
    print()


print("--------------------------------------")  

reptil_1=Reptil("Rana")
reptil_2=Reptil("Vibora")
reptil_3=Reptil("Cocodrilo")

reptil_1=reptil_2
reptil_2=reptil_3

print(reptil_1==reptil_2,reptil_2 is reptil_2)

print(reptil_1==reptil_3, reptil_2 is reptil_3)

print(reptil_1==reptil_3, reptil_1 is reptil_3)