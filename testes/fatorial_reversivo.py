import tkinter as tk
from tkinter import messagebox

def fatorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def calcular_fatorial():
    try:
        n = int(entry.get())
        resultado = fatorial_iterativo(n)
        label_resultado.config(text=f"Fatorial de {n} é: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número inteiro válido.")

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora de Fatorial")

# Cria os widgets (elementos da interface)
label_instrucao = tk.Label(janela, text="Digite um número inteiro:")
label_instrucao.pack(pady=5)

entry = tk.Entry(janela)
entry.pack(pady=5)

btn_calcular = tk.Button(janela, text="Calcular Fatorial", command=calcular_fatorial)
btn_calcular.pack(pady=10)

label_resultado = tk.Label(janela, text="")
label_resultado.pack(pady=5)

# Inicia o loop da interface
janela.mainloop()
