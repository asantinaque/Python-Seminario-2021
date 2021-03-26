linea = (input("Ingrese una frase para analizar"))
linea = linea.casefold()
x = linea.split()
y = input("ingrese palabra para contar")
y = y.casefold()

count = 0
contadorPalabra = 0

while count < len(x):
    if x[count] == y:
        contadorPalabra += 1
    count += 1
print("Su palabra:", y, "aparecio: ", contadorPalabra, "veces")
