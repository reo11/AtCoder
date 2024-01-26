def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


a, b = map(int, input().split())

if a == b:
    print(1)
else:
    count = 0
    while True:
        g = gcd(a, b)
        a = a // g
        b = b // g
        ts = []
        for div in make_divisors(abs(a - b)):
            if div == 1 or a % div == 0:
                continue
            ts.append(a % div)
        if len(ts) > 0:
            t = min(ts)
        else:
            t = min(a, b)
        a -= t
        b -= t

        count += t
        if a < 1 or b < 1:
            break
    print(count)
