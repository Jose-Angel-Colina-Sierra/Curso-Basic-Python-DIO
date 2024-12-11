class Vehiculo:
    def __init__(self,cor, placa, qnt_rodas,qnt_passageiro):
        self.cor = cor
        self.placa = placa
        self.roda = qnt_rodas
        self.passageiros = qnt_passageiro

    def ligar_motor(self):
        if self.__class__.__name__ == "Carro":
            print("Ligando Motor do carro")
        elif self.__class__.__name__ == "Caminhao":
            print("Ligando Motor do Caminhao")
        else:
            print("Ligando Motor da moto")

    def __str__(self):
        color = self.cor
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}, cor={color}"


class Motocicleta(Vehiculo):
    pass

class Carro(Vehiculo):
    pass

class Caminhao(Vehiculo):
    def __init__(self,cor, placa, qnt_rodas,qnt_passageiro,carregado):
        super().__init__(cor,placa,qnt_passageiro,qnt_rodas)
        self.carregado = carregado

    def esta_carregado(self):
            print(f'{"Sim" if self.carregado else "Nao"} estou carregado')

    

moto = Motocicleta("Black","CTX-456",2,2)
carro = Carro("white","xxx-123",4,7)
caminhao = Caminhao("blue","zzz-678",16,3,True)

print(carro)
print(moto)
print(caminhao)
