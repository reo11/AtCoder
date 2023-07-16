from math import ceil, sqrt


def solve():
    n = int(input())

    for i in range(2, ceil(n ** (1 / 3)) + 1):
        div = n // i
        if n % i ** 2 == 0:
            p = i
            q = n // i ** 2
            break
        elif n % i == 0 and int(sqrt(div)) ** 2 == div:
            p = int(sqrt(div))
            q = i
            break
    return f"{p} {q}"


t = int(input())
ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep="\n")
