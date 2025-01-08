try:

    y=1/0

except (ZeroDivisionError,ArithmeticError):
    print("Error: hubo un problema al dividir")
except:
    print("Error desconocido")

print("FIN")
