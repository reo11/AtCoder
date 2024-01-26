n, d, w = map(int, input().split())
tx = []

for _ in range(n):
    t, x = map(int, input().split())
    tx.append((t, x))

tx.sort()
