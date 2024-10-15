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


bicicleta1 = Bicicleta("marron","Praia",2018,3000)

Bicicleta.correr(bicicleta1) # -> E o mesmo, funciona para referenciar o mesmo objeto (self)
bicicleta1.parar()           # -> E o mesmo, funciona para referenciar o mesmo objeto (self)
bicicleta1.buzinar()
print(bicicleta1.cor,bicicleta1.ano,bicicleta1.modelo,bicicleta1.valor)

print("cambie")