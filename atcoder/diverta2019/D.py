n = int(input())
ans = 0
if n < 3:
    ans = 0
else:
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == n // i:
            ans += i
        i = (n // i) - 1
        if n % i == n // i:
            ans += i

print(ans)
