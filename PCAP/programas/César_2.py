# Cifrado César.
texto = input("Ingresa tu mensaje: ")

while True:
    desplazamiento = int(input("Ingresa la clave: "))
    if desplazamiento in range(1, 26):
        break

cifrado = ''
for caracter in texto:
    if not caracter.isalpha():  # si no es una letra, se mantiene igual
        cifrado += caracter
        continue
    if caracter.islower():  # si es minúscula
        codigo = ord(caracter) + desplazamiento
        if codigo > ord('z'):  # si rebasa el alfabeto minúsculo
            codigo = ord('a') + (codigo - ord('z') - 1)
    else:  # si es mayúscula
        codigo = ord(caracter) + desplazamiento
        if codigo > ord('Z'):  # si rebasa el alfabeto mayúsculo
            codigo = ord('A') + (codigo - ord('Z') - 1)
    cifrado += chr(codigo)

print("Mensaje cifrado:", cifrado)

# Descifrado César.
descifrado = ''
for caracter in cifrado:
    if not caracter.isalpha():  # si no es una letra, se mantiene igual
        descifrado += caracter
        continue
    if caracter.islower():  # si es minúscula
        codigo = ord(caracter) - desplazamiento
        if codigo < ord('a'):  # si está por debajo de 'a'
            codigo = ord('z') - (ord('a') - codigo - 1)
    else:  # si es mayúscula
        codigo = ord(caracter) - desplazamiento
        if codigo < ord('A'):  # si está por debajo de 'A'
            codigo = ord('Z') - (ord('A') - codigo - 1)
    descifrado += chr(codigo)

print("Mensaje descifrado:", descifrado)