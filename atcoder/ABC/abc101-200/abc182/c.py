a = list(map(int, list(input())))

# bit全探索
ans = float("inf")
for i in range(1, 2 ** len(a)):
    count = 0
    for j in range(len(a)):
        if i >> j & 1:
            count += a[j]
    if count % 3 == 0:
        ans = min(ans, len(a) - bin(i).count("1"))
print(ans if ans != float("inf") else -1)