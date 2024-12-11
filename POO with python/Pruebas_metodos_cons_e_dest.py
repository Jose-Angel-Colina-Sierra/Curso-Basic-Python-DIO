class Cachorro():

    def __init__(self, nome, cor, acordado=True):

        print("Inicializando a classe.....")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def falar(self):
        print("uau uau")
        print("O cachorro esta latindo")

    def __del__(self):
        print("Removendo a Instancia da Classe.")


def criar_cachorro():
    c = Cachorro("Gordo","Preto")
    print(c.nome)

c = Cachorro("Manchas","Branco")

c.falar()


print("Ola Mundo")
print("Ola Mundo")
del c
print("Ola Mundo")
print("Ola Mundo")
print("Ola Mundo")

