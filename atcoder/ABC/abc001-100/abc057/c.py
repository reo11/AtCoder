n = int(input())
def f(a, b):
    return max(len(str(a)), len(str(b)))

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

l = make_divisors(n)

ans = 10**10
for v in l:
    ans = min(ans, f(v, n//v))
print(ans)
