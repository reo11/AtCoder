n, l = map(int, input().split())

taste = []

for i in range(1, n + 1):
    taste.append(l + i - 1)

taste.sort(key=lambda x: abs(x))

print(sum(taste[1:]))
