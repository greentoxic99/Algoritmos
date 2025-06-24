#https://www.youtube.com/watch?v=cgeIryTBxAU
""" Dado um número inteiro num, a tarefa é descobrir quantos passos seriam necessários
    para reduzir esse número a zero. A regra para cada etapa do processo de redução é simples:
        Se numfor par, divida por 2.
        Se numfor ímpar, subtraia 1 dele.
    O processo é repetido até numque chegue a zero e precisamos contar
    e retornar o número total de passos dados. """

import time

def calcular_passos(num):
    passos = 0
    while num != 0:
        num = num // 2 if num % 2 == 0 else num - 1
        passos += 1
    return passos

# Entrada inicial
num = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

# Medir o tempo de execução
start_time = time.time()
passos = calcular_passos(num)
end_time = time.time()

# Exibir resultados
total_time_ms = (end_time - start_time) * 1000
print(f"Passos dados: {passos}")
print(f"Tempo total gasto: {total_time_ms:.4f} milissegundos")