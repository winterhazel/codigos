# Função recursiva que resolve Fibonacci
def fibonacci(n):
    if not (isinstance(n, int) and n >= 0):
        raise ValueError("n deve ser maior ou igual a 0")

    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(0), fibonacci(1), fibonacci(2), fibonacci(3), fibonacci(5), fibonacci(6))
