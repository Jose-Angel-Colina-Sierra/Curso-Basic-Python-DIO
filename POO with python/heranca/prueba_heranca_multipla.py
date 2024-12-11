class Animal:
    def __init__(self, nro_patas, qtd_olhos):
        self.nro_patas = nro_patas
        self.qtd_olhos = qtd_olhos

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

    def __str__(self):
        return "Mamifero 123"


class Ave(Animal):
    def __init__(self, cor_bico,**kw):
        
        self.cor_bico = cor_bico
        super().__init__(**kw)

    def __str__(self):
        return "ave 42"


class Gato(Mamifero):
    pass

class FalarMixin():
    def falar(self):
        return "estou falando"

class Ornitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_bico, cor_pelo, nro_patas, qtd_olhos):
        # Chama o construtor de Mamifero e Ave através do super()
        super().__init__(cor_pelo=cor_pelo, nro_patas=nro_patas, qtd_olhos=qtd_olhos, cor_bico=cor_bico)
        print(Ornitorrinco.__mro__)

    def __str__(self):
        return "soy yo primero"

# Criando um Gato
gato = Gato(nro_patas=4, cor_pelo="Preto", qtd_olhos=2)
# print(gato)

# Criando um Ornitorrinco
ornitorrinco = Ornitorrinco(cor_bico="laranja", cor_pelo="vermelho", nro_patas=2, qtd_olhos=2)
print(ornitorrinco.falar())
