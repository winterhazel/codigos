# Função linear que resolve Fibonacci
def fibonacci(n):
    if not (isinstance(n, int) and n >= 0):
        raise ValueError("n deve ser maior ou igual a 0")

    if n == 0 or n == 1:
        return n
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


print(fibonacci(0), fibonacci(1), fibonacci(2), fibonacci(3), fibonacci(5), fibonacci(6))
