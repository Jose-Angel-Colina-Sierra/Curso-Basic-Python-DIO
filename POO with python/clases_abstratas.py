from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass
    @property
    @abstractproperty
    def marca():
        pass

class ControleTV(ControleRemoto):
    
    def ligar(self):
        print("ligando a tv") 
    
    def desligar(self):
        print("desligando a tv") 

    @property
    def marca(self):
        return "Samsung"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("ligando o ar") 
    
    def desligar(self):
        print("desligando o ar") 
    @property
    def marca(self):
        return "LG"

controletv = ControleTV()

controletv.ligar()
controletv.desligar()

controleArCondicionado = ControleArCondicionado()
controleTV = ControleTV()

print(controleArCondicionado.marca)
print(controleTV.marca)