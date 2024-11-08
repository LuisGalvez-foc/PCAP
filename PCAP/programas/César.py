# Cifrado César.
texto = input("Ingresa tu mensaje: ")
cifrado = ''
for caracter in texto:
    if not caracter.isalpha():  # si no es una letra, se mantiene igual
        cifrado += caracter
        continue
    caracter = caracter.upper()  # convertir a mayúsculas
    codigo = ord(caracter) + 1  # punto de código siguiente
    if codigo > ord('Z'):  # si rebasa el alfabeto
        codigo = ord('A')  #... empieza otra vez
    cifrado += chr(codigo)

print("Mensaje cifrado:", cifrado)

# Descifrado César.
descifrado = ''
for caracter in cifrado:
    if not caracter.isalpha():  # si no es una letra, se mantiene igual
        descifrado += caracter
        continue
    caracter = caracter.upper()  # convertir a mayúsculas
    codigo = ord(caracter) - 1  # punto de código anterior
    if codigo < ord('A'):  # si está por debajo de 'A'
        codigo = ord('Z')  #... empieza otra vez
    descifrado += chr(codigo)

print("Mensaje descifrado:", descifrado)