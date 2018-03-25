import random

ITER_AMOUNT = 100


def mul(a, b, modulo):
    return ((a % modulo) * (b % modulo)) % modulo


def modulo_binary_exp(x, n, modulo):
    if n == 0:
        return 1
    if n % 2 == 0:
        x_pow = modulo_binary_exp(x, n // 2, modulo)
        return mul(x_pow, x_pow, modulo)
    else:
        return mul(x, modulo_binary_exp(x, n - 1, modulo), modulo)


def gcd(a, b):
    if b != 0:
        return gcd(b, a % b)
    else:
        return a


def fermat_primality_test(x):
    random.seed()
    a = random.randint(0, int(1e18))
    while gcd(a, x) != 1:
        a = random.randint(0, int(1e18))
    return modulo_binary_exp(a, x - 1, x) == 1


def get_next_prime(x):
    x += 1
    while True:
        is_probably_prime = True
        for i in range(0, ITER_AMOUNT):
            if not fermat_primality_test(x):
                is_probably_prime = False
                break
        if is_probably_prime:
            return x
        else:
            x += 1
