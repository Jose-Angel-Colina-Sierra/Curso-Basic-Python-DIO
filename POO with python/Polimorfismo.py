#exemplo: funcao len -> quando passados uma lista o uma string, mesmo que sendo objetos diferentes, ele conta a quantidade de elementos 

class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")


# Exemplo ruim do uso de heranca para mostrar de forma absurda como se pode utilizar os metodos.
class Aviao(Passaro):
    def voar(self):
        print("aviao esta decolando")


def plano_voo(obj):
    obj.voar()

p1 = Pardal()
a1 = Avestruz()
a2 = Aviao()

plano_voo(p1)
plano_voo(a1)
plano_voo(a2)