# def meu_decorador(funcao):  
#     def envelope(*args,**kwargs):
#         print("Faz algo antes de executar")
#         funcao(*args,**kwargs)
#         print("Faz algo despois de executar")
#     return envelope

# @meu_decorador
# def ola_mundo(parametro,saludar="hola"):
#     print(f"{saludar} {parametro}")


# ola_mundo("te quiero", saludar="Epale compita, todo besho?")


def duplicar(funcao):
    def envelope(*args,**kwargs):
        
        funcao(*args,**kwargs)
        
        return funcao(*args,**kwargs)
    
    return envelope


@duplicar
def aprender(tecnologia):
    print(f"Estou aprendendo tecnologia {tecnologia}")
    return tecnologia.upper()

aprender("python")

print(aprender("python"))