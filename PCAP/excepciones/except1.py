'''de la más concreta a la mas generica'''

try:

    y=1/0



except ZeroDivisionError:
    print("Error: Division entre cero")
except ArithmeticError:
    print("Error: Error aritmetico")
except:
    print("Error desconocido")

print("FIN")

