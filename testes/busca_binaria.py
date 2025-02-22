def busca_binaria(lista, valor):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == valor:
            return meio  # Retorna o índice do valor
        elif lista[meio] < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1  # Retorna -1 se o valor não for encontrado

# Teste da função
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  # Lista ordenada
valor_procurado = 7

indice = busca_binaria(lista, valor_procurado)

# Exibindo o resultado
if indice != -1:
    print(f"Valor {valor_procurado} encontrado no índice {indice}.")
else:
    print(f"Valor {valor_procurado} não encontrado na lista.")