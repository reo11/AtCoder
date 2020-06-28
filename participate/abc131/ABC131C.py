from fractions import gcd

def lcm(x, y):
    return (x * y) // gcd(x, y)

a, b, c, d = map(int, input().split())
g = lcm(c, d)

alpha_c = a % c
count_c = (b - a + alpha_c) // c
if alpha_c == 0:
    count_c += 1
alpha_d = a % d
count_d = (b - a + alpha_d) // d
if alpha_d == 0:
    count_d += 1
alpha_g = a % g
count_g = (b - a + alpha_g) // g
if alpha_g == 0:
    count_g += 1

s = b - a + 1 - count_c - count_d + count_g

print(s)
