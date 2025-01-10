def read_int(prompt, min, max):
    while True: 
        try:
            v = int(input(prompt))
            if min <= v <= max:
                return v
            else:
                print("El número ingresado no está dentro del rango permitido.")
        except ValueError:
            print("ERROR entrada incorrecta. Por favor, ingresa un número entero.")

v = read_int("Ingresa un número entre -10 y 10: ", -10, 10)

print("El número es", v)