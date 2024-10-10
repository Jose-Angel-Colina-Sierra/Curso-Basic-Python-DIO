def somar(a,b):
    return a + b

def multiplicar(a,b):
    return a * b

def test(a,b):
    return a*2 + b*2

def exibir_resultado(a, b , funcao, *, nome="none"):

    valor_da_soma = funcao(a,b)
    nome = "Jose"

    print(f"{nome} O resultado da operacao e {valor_da_soma}")


exibir_resultado(10,10,somar)
exibir_resultado(10,10,multiplicar)
exibir_resultado(10,10,test)

op = somar(12,18)

print(op)


salario = 2500
lista = list("zanahoria")

def acrescentar_bonus(bonus,lista):
    
    
    print(lista)
    global salario

    
    salario =+  bonus
    return f"tu salario es de {salario} y el bonus es de {bonus}, osea que este mes vas a cobrar {salario}"

print(acrescentar_bonus(500,lista))