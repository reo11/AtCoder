q = int(input())


def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


isprime = [False] * (10 ** 5 + 1)
for i in range(1, 10 ** 5 + 1):
    if isPrime(i):
        isprime[i] = True
ans = [0] * (10 ** 5 + 1)
v = 0
for i in range(1, 10 ** 5 + 1):
    if i % 2 == 1 and isprime[i] and isprime[(i + 1) // 2]:
        v += 1
    ans[i] = v
for i in range(q):
    l, r = map(int, input().split())
    print(ans[r] - ans[l - 1])
