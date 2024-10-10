#input, e uma funcao built-in e funciona com entrada de dados do usuario.

#exeplos de sep(separador entre os argumentos passados),end(que vai acontecer ao final da impresao),file(especifica um objeto de arquivo onde a saída será direcionada),flush(determina se o buffer de saída deve ser esvaziado imediatamente)

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

print(nome,sobrenome, end="...\n",sep=".")

