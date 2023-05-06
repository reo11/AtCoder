# https://mathtrain.jp/phi
from typing import List

# def euler_phi(n: int) -> int:
#     phi = n
#     unique_factorized_primes: List[int] = list(set(prime_factorize(n)))
#     for i in unique_factorized_primes:
#         phi *= 1 - (1 / i)
#     return int(phi)


# def prime_factorize(n: int) -> int:
#     # Return list of prime factorized result
#     a = []
#     while n % 2 == 0:
#         a.append(2)
#         n //= 2
#     f = 3
#     while f * f <= n:
#         if n % f == 0:
#             a.append(f)
#             n //= f
#         else:
#             f += 2
#     if n != 1:
#         a.append(n)
#     return a
