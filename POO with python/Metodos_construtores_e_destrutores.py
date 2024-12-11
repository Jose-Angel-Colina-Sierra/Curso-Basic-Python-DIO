#metodo construtor ou metodo inicializador -> __init__ 

# Serve para iniciar valores e o estado inicial da nossa clase.

class Cachorro():
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado


#metodo destrutor -> __del__

class Cachorro:

    def __del__(self):
        print("Removendo a instância da classe.")

    
c = Cachorro()

del c

#Exemplo com construtor e destrutor:


class Chachorro():

    def __init__(self, nome, cor, acordado=True):

        print("Inicializando a classe.....")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def falar(self):
        pass

c = Cachorro("Manchas","Branco")











