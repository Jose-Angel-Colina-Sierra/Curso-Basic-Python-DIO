class Bicicleta():
    def __init__(self,cor,modelo,ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor


    def buzinar(seld):
        print("Piiiiii piiiiii!!!")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

    
    def __str__(self):
        return f"{self.__class__.__name__}: {[f'{chave}={valor}' for chave, valor in self.__dict__.items()]}"


bicicleta1 = Bicicleta("marron","Praia",2018,3000)

# Bicicleta.correr(bicicleta1) # -> E o mesmo, funciona para referenciar o mesmo objeto (self)
# bicicleta1.parar()           # -> E o mesmo, funciona para referenciar o mesmo objeto (self)
# bicicleta1.buzinar()
# print(bicicleta1.cor,bicicleta1.ano,bicicleta1.modelo,bicicleta1.valor)


print(bicicleta1)