n = int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if i == n:
            continue
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                if n // i == n:
                    continue
                divisors.append(n // i)
    return sorted(divisors)

# 約数列挙
divs = list(make_divisors(n)) + [n]

ans = []
for i in range(n + 1):
    ansi = "-"
    for j in divs:
        if j >= 10:
            break
        if i % (n // j) == 0:
            ansi = str(j)
            break
    ans.append(ansi)
print("".join(ans))
