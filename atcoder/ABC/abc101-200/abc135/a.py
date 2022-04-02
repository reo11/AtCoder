a, b = map(int, input().split())

k = (a + b) // 2

if abs(a - k) == abs(b - k):
    print(k)
else:
    print("IMPOSSIBLE")
