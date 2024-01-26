import sys

input = lambda: sys.stdin.readline().rstrip()
INF = float("inf")

n, x = map(int, input().split())
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append((a, b))

# i番目のbを使用してカンストさせる時の最小値

ans = INF
ab_sum = 0  # i - 1番目までのa + bの合計値
for i in range(n):
    a, b = ab[i]
    if i > x:
        break
    ans = min(ans, ab_sum + a + (b * (x - i)))
    ab_sum += a + b

print(ans)
