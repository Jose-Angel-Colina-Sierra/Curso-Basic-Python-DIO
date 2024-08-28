import sys #modulo sys

#Elas permitem o desvio de fluxo de controle, quando uma expressao logica se cumpre ou nao.

#Etapa1 if / if-else/ elif
#Etapa2 if aninhado
#Etapa3 if ternário


#Exemplos:

#1

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print('Saque realizado')

if saldo < saque:
    print('Saldo insuficiente')

#2

if saldo >= saque:
    print('Saque realizado')
else: #utilizacao do else
    print('Saldo insuficiente')

#3 

opcao = int(input("informe uma opcao: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
    # ...
elif opcao == 2: #utilizacao do elif
    print(f"O valor da sua conta é {saldo}")
else:
    sys.exit("Opcao invalida")

#4

maior_idade = 18

idade = int(input("Informe sua idade: "))

if idade >= maior_idade:
    print("Pode Tirar CNH")
else:
    print("Nao pode tirar CNH")

#5

maior_idade2 = 18
idoso = 60

idade = int(input("Informe sua idade: "))

if idade >= maior_idade2 and idade <= idoso:
    print("Pode Tirar CNH")
elif idade >= idoso:
    print("Pode tirar CNH Especial")
else:
    print("Nao pode tirar CNH, meu xovem")

#6

Nota_1, Nota_2, Nota_3 = float(input("Digite sua primeira nota")), float(input("Digite sua segunda nota")), float(input("Digite sua terceira nota"))


soma_notas = Nota_1 + Nota_2 + Nota_3

media_nota = soma_notas / 3

estudiante_problema = "Daniel"
estudiante_ejemplar = "Jose"

estudiante = input("Digite seu primeiro nome: ")

if estudiante == estudiante_ejemplar:
    if media_nota >= 9:
        print("Felicitaciones mijito no esperaba menos")
    elif media_nota < 9 and media_nota >= 6:
        print("Esperaba mas, pero asi son las vainas")
    else:
        print(f"Que decepcion {estudiante_ejemplar}, esperaba mas de usted")
else:
    if media_nota >= 9:
        print("Asi habra lamboniado")
    elif media_nota < 9 and media_nota >= 6:
        print("Buena papito, se esforzo bastante")
    else:
        print(f"como siempre, yo no se que valores le he ensenado")    
