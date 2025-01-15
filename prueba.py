#EXERCICIO 1 -----------------------------------------------------------------------------------------------


# TODO: Crie uma classe e método para realizar a soma:

class Calculadora:
    def soma(self,numero1,numero2):
        self._numero1 = numero1
        self._numero2 = numero2

        soma_operacao = self._numero1 + self._numero2
        return soma_operacao
    

num1 = int(input())
num2 = int(input())

# Criando uma instância da calculadora
calc = Calculadora()

resultado = calc.soma(num1, num2)
print(resultado)


#EXERCICIO 2 -----------------------------------------------------------------------------------------------

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def formatar_nome(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

#TODO: Crie um método para retornar as informações formatas com Nome e Idade:    
    

# Entrada do usuário
nome = input()
idade = int(input())

# TODO: Crie uma instância da pessoa:

pessoa = Pessoa(nome, idade)

#TODO: Chame o método para retornar as informações formatadas e imprima o resultado:

print(pessoa.formatar_nome())



#EXERCICIO 3 -----------------------------------------------------------------------------------------------


#TODO: Crie uma classe para converter temperaturas de Celsius para Fahrenheit e um método que realiza o cálculo de conversão:

class Conversor:

    def celsius_para_fahrenheit(self, celsius):
        self.celsius = celsius
        return self.celsius * 1.8 + 32

# Entrada do usuário
celsius = float(input())

# TODO: Crie uma instância do conversor:

conversor = Conversor()

fahrenheit = conversor.celsius_para_fahrenheit(celsius)
print(fahrenheit)