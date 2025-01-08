class Pessoa:
    def __init__(self, nome):
        self.__nome = nome  

    def __comer(self):
        return "Estou comendo"  
    
    def __str__(self):
        return self.__nome  

class Trabajador(Pessoa):  
    def __init__(self, nome, trabalho):
        super().__init__(nome) 
        self.trabalho = trabalho  

    def trabalhar(self):
        return f"{self.__str__()} está trabalhando como {self.trabalho}"  


objeto = Trabajador("Jose", "Engenheiro")
print(objeto)  
print(objeto._Pessoa__comer())  
print(objeto.trabalhar())