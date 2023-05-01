n = int(input())
a, b, c = map(int, input().split())

ans = float("inf")
for a_i in range(10000):
    if n - a * a_i < 0:
        break
    for b_i in range(10000):
        if n - a * a_i - b * b_i < 0:
            break
        if (n - a * a_i - b * b_i) % c == 0:
            ans = min(ans, a_i + b_i + (n - a * a_i - b * b_i) // c)
print(ans)

