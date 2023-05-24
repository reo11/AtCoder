def euler_phi(n):
    phi = n
    for i in set(prime_factorize(n)):
        phi *= 1 - (1 / i)
    return phi


def prime_factorize(n):
    # Return list of prime factorized result
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


n = int(input())
print(int(euler_phi(n)))
