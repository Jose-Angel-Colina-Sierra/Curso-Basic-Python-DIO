import sys


#sao estruturas utilizadas para repetir um trecho e codigo, um determinado numero de vezes. Esse numero pode ser conhecido previamente ou determinado atraves de uma expressao logica.

#1 for -> e usado para percorrer um objeto iteravel, faz sentido usar for quando sabemos o numero exato de vezes que queremos que o codigo seja executado, ou quando percorre um objeto iteravel.

texto = input("informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()
    print("Executa no final do lazo")


# RANGE ------------------------------

for numero in range(0, 101, 10):
    print(numero, end=" ")

# While -> Utilizado para repetir um bloco de codigo varias vezes, faz sentido quando nao sei quantas vezes ele deve repetir.

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n"))

    if opcao == 1:
        print("Sacando dindin...")
    elif opcao == 2:
        print("Exibindo o extrato...")
    elif opcao == 0:
        print("Voce saiu do sistema...")    
    else:
        sys.exit("Opcao nao disponivel")
else:
    print("Obrigado por utilizar nosso sistema")


#break - Corta o lazo da execucao se uma logica for atendida --------------------------

while True:
    numero = int(input("informe un numero: "))

    if numero == 10:
        break

#exemplo 2 break

for numero in range(100):
    if numero == 99:
        break
    print(numero, end=" ")

#Continue - desviar de alguma situaao especifica do bucle -----------------------------------

for numero in range(27):
    if numero == 23:
        continue
    print(numero, end=" ")