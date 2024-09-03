curso = "PytHon"

#Todos para maiusculo
print(curso.upper())

#Todos para minusculo
print(curso.lower())

#Todos para maiusculo, exeto da primeira letra
print(curso.title())

curso2 = "    PytHon"

#Tira todo os espacos

print(curso2.strip())

#Tira todo os espacos LEFT

print(curso2.lstrip())

#Tira todo os espacos RIGHT

print(curso2.rstrip())

#juncao e centralizacao de string:

curso3 = "Python"

print(curso3.center(10, "#")) #-> se nao informar nenhum caracter ele adiciona um spaco em branco

print((curso3.center(10, "#")))

for letra in menu:
    print(letra, end=""     )


string = '''hola
hioalan
haoaol,'''