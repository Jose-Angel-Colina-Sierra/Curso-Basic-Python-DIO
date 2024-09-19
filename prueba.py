numeros = [1, 30, 25, 22, 40, 34, 35, 26, 278, 28, 29]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)


print(pares)

numeros = [1, 30, 25, 22, 40, 34, 35, 26, 278, 28, 29]

pares = [float(numero/2) for numero in numeros if numero % 2 == 0]

print(pares) 



