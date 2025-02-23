# pino A = origem
# pino B = destino
# pino C = trabalho
# n discos de tamanhos diferentes

# todos os discos estão em origem A
    # em ordem decrescente de tamanho (de baixo para cima)


# Objetivo: empilhar todos os discos no pino destino B
    # Restrições:
    # 1) apenas 1 disco movido por vez
    # 2) qualquer disco não pode ser colocado sobre outro de tamanho menor


def hanoi(n, A, B, C):
    if n > 0:
        hanoi(n - 1, A, C, B)
        print(f"Mova o disco {n} de {A} para {B}")
        hanoi(n - 1, C, B, A)


n = 2

hanoi(n, 'A', 'B', 'C')

def count_hanoi_moves(n):
    if n == 0:
        return 0
    return 2 * count_hanoi_moves(n - 1) + 1

moves = count_hanoi_moves(n)
print(f"Total de movimentos: {moves}")