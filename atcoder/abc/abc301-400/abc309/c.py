import sys

input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
ab = []

for _ in [0] * n:
    a, b = map(int, input().split())
    ab.append((1, b))
    ab.append((a + 1, -b))

# imos
ab.sort()
# print(ab)
count = 0
day = 1
for a, b in ab:
    if a == 1:
        count += b
        continue
    else:
        # day1で条件を満たしている場合用
        if count <= k:
            break
        day = a
        count += b

print(day)
