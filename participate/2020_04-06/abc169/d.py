from collections import Counter
n = int(input())
def prime_factorize(n):
    # Return list of prime factorized result
    # O(sqrt(n))
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
l = prime_factorize(n)
cnt = Counter(l)

ans = 0
for key in cnt.keys():
    cur = 1
    while True:
        if cnt[key] >= cur:
            cnt[key] -= cur
            ans += 1
            cur += 1
        else:
            break
print(ans)
