from typing import List


def prime_factorize(n: int) -> List[int]:
    # 素因数分解
    # Return list of prime factorized result
    # O(sqrt(n))
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


if __name__ == "__main__":
    n = int(input())
    print(" ".join(map(str, prime_factorize(n))))
