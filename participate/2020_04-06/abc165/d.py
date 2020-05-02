a, b, n = map(int, input().split())
start = min(b - 1, n)
def f(x):
    return int(a * x / b) - a * int(x / b)
print(f(start))