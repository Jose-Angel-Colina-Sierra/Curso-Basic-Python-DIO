#identar e uma forma de manter o codifo fonte mais legivel e manutenivel, e em python a identacao e obrigatorio.


#exemplo ->

def sacar(self,valor: float) -> None:
    if self.saldo >= valor:
        self.saldo -= valor



#boas praticas -> 4 espacos em branco para cada bloco de identacao.

def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print('Sacando el valor!')

sacar(20)

