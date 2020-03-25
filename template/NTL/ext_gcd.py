def extgcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, y, x = extgcd(b, a%b)
        y -= a // b * x
        return d, x, y