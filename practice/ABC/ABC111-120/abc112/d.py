n, m = map(int, input().split())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

ans = 1
for v in make_divisors(m):
    if v <= m / n:
        ans = max(ans, v)
print(ans)