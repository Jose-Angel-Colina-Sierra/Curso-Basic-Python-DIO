class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.escola} - {self.matricula} "
    
estudante = Estudante("Jose",2222233344)
estudante2 = Estudante("Daniel",55555533344)


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

mostrar_valores(estudante,estudante2)

estudante.nome = "Fernando"
estudante2.nome = "Carlos"

Estudante.escola = "Alura"

mostrar_valores(estudante,estudante2)

estudante.escola = "udemy" # isso esta errado , nao estou 

mostrar_valores(estudante,estudante2)