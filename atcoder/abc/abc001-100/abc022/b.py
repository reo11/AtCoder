n = int(input())
d = [0] * (10 ** 5 + 1)
count = 0
for _ in range(n):
    a = int(input())
    if d[a] > 0:
        count += 1
    d[a] += 1

print(count)
