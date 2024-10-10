def contar_caracteres(string):
    # Inicializa um dicionário vazio 'contador' para armazenar as contagens de caracteres.
    contador = {}

    # Itera através de cada caractere na string.
    for caractere in string:
        # Verifica se o caractere já está presente no dicionário contador:
        if caractere in contador:
            contador[caractere] += 1  # Incrementa o valor se o caractere já está no dicionário
        else:
            contador[caractere] = 1  # Adiciona o caractere ao dicionário com valor inicial 1

    return contador