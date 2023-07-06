def fibonacci(n):
    sequence = []
    if n == 0:
        return sequence
    elif n == 1:
        sequence.append(0)
        return sequence
    else:
        sequence = [0, 1]
        while len(sequence) < n:
            next_number = sequence[-1] + sequence[-2]
            sequence.append(next_number)
        return sequence

# Leitura do número inteiro N
n = int(input("Digite um número inteiro: "))

# Chamada da função para obter a sequência de Fibonacci
fibonacci_sequence = fibonacci(n)

# Exibição dos N primeiros elementos da sequência de Fibonacci
print("Sequência de Fibonacci com os", n, "primeiros elementos:")
for number in fibonacci_sequence:
    print(number)