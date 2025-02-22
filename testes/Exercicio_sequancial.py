def buscar_numero(lista, numero):
    for i in range(len(lista)):
        if lista[i] == numero:
            return True
    return False
    
lista = [10,11,12,13,14,15,16,17,18,19,20]

try:
    numero = int(input('Digite um número: '))
    resultado = buscar_numero(lista, numero)
    print(resultado)
except ValueError:
    print('Digite apenas números inteiros.')