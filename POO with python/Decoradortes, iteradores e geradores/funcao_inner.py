def principal():
    print("Executando a funcao principal")

    texto = int(input("Escreva o numero da funcao que vc quer (1 ou 2): "))

    def executando_funcao_interna_1():
        print("Executando a funcao interna 1")

    def executando_funcao_interna_2():
        print("Executando a funcao interna 2")

    
    if texto == 1:
        executando_funcao_interna_1()
    elif texto == 2:
        executando_funcao_interna_2()
    else:
        print("Opção inválida!")

principal()
