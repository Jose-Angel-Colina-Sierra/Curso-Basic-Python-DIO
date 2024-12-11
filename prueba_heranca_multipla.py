class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas     

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"            

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(nro_patas=kw["nro_patas"])
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self,cor_bico, **kw):
        super().__init__(nro_patas=kw["nro_patas"])

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    pass

# Criando objetos e testando
gato = Gato(4, "preta")
loro = Ave(2)
ornitorrinco = Ornitorrinco(4, "marrom","Laranja")

print(gato)
print(loro)
print(ornitorrinco)

