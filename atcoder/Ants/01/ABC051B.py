k, s = map(int, input().split())
count = 0
for x in range(k + 1):
    for y in range(k + 1):
        if 0 <= s - (x + y) <= k:
            count += 1
print(count)
