def fact(n, mod):
    r = 1
    for i in range(2, n):
        r *= i
        r %= mod
    return r