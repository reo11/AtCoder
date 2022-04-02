a, b, k, l = map(int, input().split())

ans = min((k // l) * b + (k % l) * a, (k // l + 1) * b)
print(ans)
