from math import factorial
n, a, b ,c = map(int, input().split())
mod = 10**9 + 7

def comb(n, r):
    return factorial(n) / factorial(r) / factorial(n - r)

e = 0
for m in range(n, 2*n):
    e += comb(m - 1, n - 1) * (a**n * b**(m-n) + a**(m-n) * b**n) * m / (100**(n-1) * (100 - c))
print(e)

# if a == 0 or b == 0:
#     print(n)
# else:
#     p = 0
#     for i in range(n):
#         p += i * comb*(a + b)*(1 - (c/100)**n)
#     q = (100 - c)*(1 - (c/100))**2

#     print(p, q, p/q)

