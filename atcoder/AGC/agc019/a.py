q, h, s, d = map(int, input().split())
n = int(input())

one_cost = min(q * 4, h * 2, s)
two_cost = d

ans = n // 2 * min(two_cost, one_cost * 2)

if n % 2:
    ans += one_cost
print(ans)
