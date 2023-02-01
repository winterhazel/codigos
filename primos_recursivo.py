# Função recursiva que encontra primos
def primes_up_to(n, start=2, primes=[]):
    if not (isinstance(n, int) and n > 1):
        raise ValueError("n deve ser um inteiro maior que 1")

    for p in primes:
        if start % p == 0:
            break
    else:
        # for terminou sem um break
        # Isto significa que o número atual não é divisível por nenhum número na lista de primos
        primes.append(start)
    return primes.copy() if n <= start else primes_up_to(n, start + 1, primes)


print(primes_up_to(2), primes_up_to(3), primes_up_to(10))
