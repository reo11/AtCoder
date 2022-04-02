r, g, b, n = map(int, input().split())

ans = 0

for i in range(3001):
    if i * r > n:
        break
    for j in range(3001):
        value = r * i + g * j
        if (n - value) < 0:
            break
        elif (n - value) % b == 0:
            ans += 1
print(ans)
