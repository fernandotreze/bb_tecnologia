def busca_sequencial(lista, valor):
    for i in range(len(lista)):  # Passo 1
        if lista[i] == valor:  # Passo 2
            return i  # Passo 3
    return -1  # Passo 4

# Testando a função
lista = [10, 20, 30, 40, 50]
valor = 30
resultado = busca_sequencial(lista, valor)
print(f'O valor {valor} foi encontrado no índice {resultado}')
