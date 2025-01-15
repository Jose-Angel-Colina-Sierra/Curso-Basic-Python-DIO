def mensagem(nome):
    print("Executando nome")
    return f"Oi {nome}"


def mensagem_longa(nome):
    print("Executando mensagem longa")
    return f"ola tudo bem com voce {nome} ?"

def executar(funcao, nome):
    print("executando executar")
    return funcao(nome)



print(executar(mensagem, "Jose"))
print(executar(mensagem_longa, "Jose"))