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


numeros = [1, 30, 25, 22, 40, 34, 35, 26, 278, 28, 29]

pares = [float(numero/2) for numero in numeros if numero % 2 == 0]

print(pares)

#append:

lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)  # [1, "Python", [40, 30, 20]]

#clear:

lista = [1, "Python", [40, 30, 20]]

print(lista)  # [1, "Python", [40, 30, 20]]

lista.clear()

print(lista)  # []

#Copy:

lista = [1, "Python", [40, 30, 20]]

lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

#count:

cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1

#extend:

linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]

#index: -> vai ser o primeiro match

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0

#pop: - Funciona como uma pilha

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())  # csharp
print(linguagens.pop())  # java
print(linguagens.pop())  # c
print(linguagens.pop(0))  # python

#remove

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens)  # ["python", "js", "java", "csharp"]


#reverse -> faz o espelhamento - mesma coisa que se pode fazer com o slice

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.reverse()

print(linguagens)  # ["csharp", "java", "c", "js", "python"]


#sort -> organiza a lista

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)

#parametros ->

#reverse ou key

#reverse=true vaio fazer o espelhamento /// reverse=false nao vai espelhar

#key 

#len

linguagens = ["python", "js", "c", "java", "csharp"]

print(len(linguagens))  # 5

#sorted

#sortedlinguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]