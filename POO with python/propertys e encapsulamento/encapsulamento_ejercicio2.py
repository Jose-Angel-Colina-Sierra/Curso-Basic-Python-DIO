class Conta():
    def __init__(self, saldo=0):
        self._saldo = saldo

    def depositar(self):
        pass
    def sacar(self):
        pass


conta = Conta(100)

print(conta._saldo)