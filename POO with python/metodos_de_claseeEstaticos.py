class Pessoa:
    def __init__(self,nome=None,idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_data_nascimento(cls,ano,mes,dia,nome):
        idade = 2025 - ano
        return cls(nome, idade)
    
    @staticmethod

    def e_maior_de_idade(idade):
        if idade >= 18:
            return "E Maior de idade"
        else:
            return "Nao e maior de idade"

# pessoa  = Pessoa("Jose", 23)
# print(pessoa.nome, pessoa.idade)


pessoa2 = Pessoa.criar_data_nascimento(2001, 2, 7, "Jose") 

print(pessoa2.idade, pessoa2.nome, pessoa2.e_maior_de_idade(pessoa2.idade))
