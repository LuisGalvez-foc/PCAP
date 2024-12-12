tablero=[]
sudoku_ok=False

for i in range(9):
    fila = input("introduce fila "+str(i)+" :")
    if not fila.isnumeric():
        print("Error, solo se permiten digitos")
        break
    elif sorted(fila) != list("123456789"):
        print(sorted(fila))
        print("la fila debe contener los digitos del intervalo [1-9]")
        break
    else:
        sudoku_ok=True
        tablero.append(fila)

if sudoku_ok:
    print("valido")
else:
    print("no valido")

    
