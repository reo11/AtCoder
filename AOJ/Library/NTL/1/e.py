def extgcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, y, x = extgcd(b, a % b)
        y -= a // b * x
        return d, x, y


a, b = map(int, input().split())
_, x, y = extgcd(a, b)
print(x, y)
