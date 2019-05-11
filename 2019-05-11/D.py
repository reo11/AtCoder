n = int(input())
ans = 0
if n < 3:
    ans = 0
else:
    i = n - 1
    while i > 1:
        if n % i == n // i:
            ans += i
        i -= 1

print(ans)