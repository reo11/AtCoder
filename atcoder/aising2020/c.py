n = int(input())
ans = []
f = [0 for _ in range(10**4 + 1)]
for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            tmp = x**2 + y**2 + z**2 + x * y + y * z + z * x
            if tmp <= n:
                f[tmp] += 1
for i in range(1, n + 1):
    ans.append(str(f[i]))
print("\n".join(ans))
