def InverterVetor(lista):
    n - len(lista)
    for i in range(n // 2):
        lista[i], lista[n - i - 1] = lista[n - i - 1], lista[i]


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


InverterVetor(lista)

print(lista)
