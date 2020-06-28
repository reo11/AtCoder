def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(x, y):
    return (x * y) // gcd(x, y)

a, b  = map(int, input().split())

print(lcm(a, b))