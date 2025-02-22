def dividir(a, b):
    try:
        return a / b  # Tenta dividir
    except ZeroDivisionError:  # Se der erro, executa isso
        return "Erro: divisão por zero!"

print(dividir(10, 2))  # ✅ Retorna 5.0
print(dividir(10, 0))  # ✅ Retorna "Erro: divisão por zero!" em vez de quebrar o código.
