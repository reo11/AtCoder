a, b, c, d, e, f, x = map(int, input().split())


def func(a, b, c, x):
    return ((x // (a + c)) * a * b) + (min(x % (a + c), a) * b)


if func(a, b, c, x) > func(d, e, f, x):
    print("Takahashi")
elif func(a, b, c, x) < func(d, e, f, x):
    print("Aoki")
else:
    print("Draw")
