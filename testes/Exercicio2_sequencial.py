def buscar_indices(lista, valor):
    primeiro_indice = -1
    ultimo_indice = -1
   
    for i, elemento in enumerate(lista):
        if elemento == valor:
            if primeiro_indice == -1:
                primeiro_indice = i
            ultimo_indice = i
    return (primeiro_indice, ultimo_indice)

# Testes
lista = [4, 2, 7, 2, 9, 2, 5]
valor = 2
assert buscar_indices(lista, valor) == (1, 5)  # Teste para encontrar o primeiro e último índice do valor 2 na lista

lista = [1, 2, 3, 4, 5, 6, 7, 2, 9, 10]
valor = 2
assert buscar_indices(lista, valor) == (1, 7)  # Teste para encontrar o primeiro e último índice do valor 2 na lista

lista = [1, 3, 5, 7, 9]
valor = 2
assert buscar_indices(lista, valor) == (-1, -1)  # Teste para verificar que o valor 2 não está presente na lista