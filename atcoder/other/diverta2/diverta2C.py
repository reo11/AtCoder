n = int(input())
a = [int(i) for i in input().split()]
a.sort()

out = ""

minus = [a[0]]
plus = [a[-1]]

for v in a[1:-1]:
    if v < 0:
        minus.append(v)
    else:
        plus.append(v)

# (plus[0] - (minus[0] - plus[n])) - minus[n]
base_minus = minus.pop(0)
base_plus = plus.pop(0)
for i in range(len(plus)):
    x = base_minus
    y = plus[i]
    out += "{} {}\n".format(x, y)
    base_minus = x - y

out += "{} {}\n".format(base_plus, base_minus)
base_plus -= base_minus

for i in range(len(minus)):
    x = base_plus
    y = minus[i]
    out += "{} {}\n".format(x, y)
    base_plus = x - y
print(base_plus)
print(out)
