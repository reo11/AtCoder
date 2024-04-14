n = int(input())


def count_digits(x):
    x_str = list(str(x))
    ans = 0
    for xi in x_str:
        ans += int(xi)
    return ans

def check(n, x):
    for i in range(n + 1):
        print(i, 2 ** i, count_digits(2 ** i * x))

check(n, int("1101111010001101111010001101111010001101111010", 2))