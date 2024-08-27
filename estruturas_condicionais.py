import sys

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