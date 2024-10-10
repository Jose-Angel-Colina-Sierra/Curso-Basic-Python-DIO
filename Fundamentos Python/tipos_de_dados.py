#alguns tipos de variaveis: int, float, booleam, str

print(11 + 10)
print(1.4 + 32)
print(type(True))
print(type("Python"))

#clases costructora
str()
int()
float()
bool()

#exemplo que criei para utilizar o help -> no modo interativo para verificar que metodos teria minha clase Persona
class Persona:
    def __init__(self,nombre):
        self.nombre = nombre

persona = Persona("Jose")

print(persona.nombre)
print(type(persona))

nome = "Jose"
idade = 23

print(f'Hola me llamo {nome} y tengo {idade} anos de edad')

#desempacotamento de tuplas para declarar variaveis.

nome , idade = ("Daniel",35)

print(f'Hola me llamo {nome} y tengo {idade} anos de edad')


#utilizacao do snake case e especificidade na declaracao de variaveis.
limite_saque_diario = 1000


#Declaracao de constantes em PYTHON -> nao existe uma palavra reservada para a declaracao de constantes em python, ao inves disso, tem uma convencao, que determina que um dado que deve ser considerados como CONSTANTE deve declararse em uma variavel com nome em Maiuscula.

STATES = ["SP","RJ","SC","RS"]
print(STATES)

STATES = ["SP"]
print(STATES)
