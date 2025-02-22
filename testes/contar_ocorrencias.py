# Escreva uma função contar_ocorrencias(lista, valor) que conte quantas vezes o valor aparece na lista.

def contar_ocorrencias(lista, valor):
    contagem = 0
    for elemento in lista:
        if elemento == valor:
            contagem += 1
    return contagem


lista = [1, 2, 3, 2, 5, 2, 8]
valor = 2
assert contar_ocorrencias(lista, valor) == 3  # O valor 2 aparece 3 vezes na lista
