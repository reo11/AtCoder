a, b, c, d = map(int, input().split())

X = []
Y = []

# XとYにあり得る候補をいれる
X += [a]
X += [b]
if a <= 0 and 0 <= b:
    X += [0]

Y += [c]
Y += [d]
if c <= 0 and 0 <= d:
    Y += [0]

ans = -10**18
for x in X:
    for y in Y:
        ans = max(ans, x * y)
print(ans)
