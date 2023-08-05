MOD = 998244353

# https://qiita.com/drken/items/ae02240cd1f8edfc86fd
def mod(a, m):
    res = a % m
    if res < 0:
        res += m
    return res

def extGCD(a, b, p=0, q=0):
    if b == 0:
        p = 1
        q = 0
        return a, p, q
    d, q, p = extGCD(b, a%b)
    q -= a // b * p
    return d, p, q

def modinv(a, m):
    d, x, y = extGCD(a, m)
    return mod(x, m)  # 気持ち的には x % m だが、x が負かもしれないので

def garner(b, m, MOD):
    m.append(MOD)  # 番兵
    coeffs = [1 for _ in range(len(m))]
    constants = [0 for _ in range(len(m))]
    for k in range(len(b)):
        t = mod((b[k] - constants[k]) * modinv(coeffs[k], m[k]), m[k])
        for i in range(k+1, len(m)):
            constants[i] += t * coeffs[i]
            constants[i] %= m[i]
            coeffs[i] *= m[k]
            coeffs[i] %= m[i]
    return constants[-1]

n, a, b, c, d = map(int, input().split())
r = []
m = []
max_p = 0
max_q = 0
for k in range(n):
    q = (a + k * b)
    p = (c + k * d)
    max_p = max(max_p, p)
    max_q = max(max_q, q)
    r.append(p)
    m.append(q)
x = garner(r, m, MOD)
print(max_p, max_q)
print(x)