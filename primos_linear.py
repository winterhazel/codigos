# Função linear que encontra primos
# O(n) por Crivo de Eratóstenes
def primes_up_to(n):
    if not (isinstance(n, int) and n > 1):
        raise ValueError("n deve ser um inteiro maior que 1")

    primes = []
    SPF = [None] * (n + 1)
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            SPF[i] = i

        j = 0
        while (j < len(primes) and i * primes[j] <= n and primes[j] <= SPF[i]):
            is_prime[i * primes[j]] = False
            SPF[i * primes[j]] = primes[j]
            j += 1

    return primes


print(primes_up_to(2), primes_up_to(3), primes_up_to(10))
