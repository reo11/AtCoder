x, y = map(int, input().split())
N = int(input())
X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

ans = float("inf")
for i in range(N):
    a = Y[i] - Y[i - 1]
    b = X[i - 1] - X[i]
    c = Y[i - 1] * (X[i] - X[i - 1]) - X[i - 1] * (Y[i] - Y[i - 1])
    d = abs(a * x + b * y + c)
    e = (a ** 2 + b ** 2) ** 0.5
    d = d / e
    ans = min(ans, d)

print("{:.10f}".format(ans))
