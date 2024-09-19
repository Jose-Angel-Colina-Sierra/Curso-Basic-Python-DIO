frutas = ["laranja", "maca", "uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

#Matriz /////////////////////////////////////////////////////////////

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0]) 
print(matriz[0][0])  
print(matriz[0][-1])  
print(matriz[-1][-1])  


#Fatiamento/////////////////////////////////////////////////////

lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]


#Iterar Listas ////////////////////////////////////////////

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


#List Comprenhension ///////////////////////////////////////

#como normalmente faria sem o list comprehension

numeros = [1, 30, 25, 22, 40, 34, 35, 26, 278, 28, 29]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
