n, k = map(int, input().split())
v = list(map(int, input().split()))

ans = 0
for a in range(min(n, k) + 1):
    for b in range(min(n - a, k - a) + 1):
        v_use = v[:a] + v[-b:] if b >= 1 else v[:a]
        t = k - a - b
        s = 0
        for j in sorted(v_use):
            if j < 0 and t > 0:
                s += -j
                t -= 1
        ans = max(ans, sum(v_use) + s)

print(ans)
