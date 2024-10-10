# Sao utilizados em conjunto de operadores de comparacao, para montar uma expressao logica
#Sempre devolve um valor booleano false ou true

saldo = 1000
saque = 200
limite = 100
conta_especial = True

#and
True and True = True
True and False = False
False and False = False


#or
True or True = True
True or False = True
False or False = False

#not
not True = False
not False = True

#and
print(saldo >= saque and saque <= limite)

#and
print(saldo >= saque or saque <= limite)

#not -> vai fazer tipo o "inverso"
print(not saldo >= saque)

#Uso do parentesees

print((saldo >= saque and saque <= limite) or (conta_especial and saque >= limite))