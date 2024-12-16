import math

x = float(input("Ingresa un número: "))
try:  
    assert x >= 0.0
except AssertionError:
    print("error en el assert")
    exit()


x = math.sqrt(x)    

    


print(x)