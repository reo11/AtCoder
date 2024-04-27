n = int(input())
a = list(map(int, input().split()))

positions = dict()

for i in range(n):
    positions[a[i]] = i

ans = []

for i in range(1, n + 1):
    if a[i - 1] == i:
        continue
    else:
        # swap
        ans.append(f"{i} {positions[i] + 1}")
        a[positions[i]] = a[i - 1]
        positions[a[i - 1]] = positions[i]
        positions[i] = i - 1
        a[i - 1] = i
print(len(ans))
if len(ans) > 0:
    print(*ans, sep="\n")