x, y = map(int, input().split())

# area = teihen * takasa / 2
# known: area, teihen
# takasa = 2 * area / teihen
# y = ax + b
# y1 = ax + b + takasa
# b = 0
# a = y / x
# y1 = y0 / x0 * x1 + (2 / math.sqrt(x0**2 + y0**2))
# y1 * x0 = y0 * x1 + 2 * x0 / math.sqrt(x0**2 + y0**2)
# y1 * x0 * math.sqrt(x0**2 + y0**2) = y0 * x1 * math.sqrt(x0**2 + y0**2) + 2 * x0
