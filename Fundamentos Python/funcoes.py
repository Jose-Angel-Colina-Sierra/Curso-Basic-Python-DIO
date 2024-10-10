def exibir_mensagem1():
    print('Hola mundo')

exibir_mensagem1()

def exibir_mensagem2(nome):
    print(f'Hola mundo, soy {nome}')

exibir_mensagem2("Jose")

def exibir_mensagem3(nome = 'default'):
    print(f'Hola mundo, soy {nome}')

exibir_mensagem3("jose")


def calcular_total(numeros):
    return sum(numeros)

print(calcular_total([45,23]))


def retornar_antecesor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return {"antecessor": antecessor,
            "sucessor": sucessor}

resultado = retornar_antecesor_e_sucessor(24)
print(resultado)


