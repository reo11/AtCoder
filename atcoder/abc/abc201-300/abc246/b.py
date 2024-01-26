from math import sqrt

a, b = map(int, input().split())

if a != 0 and b != 0:
    y = sqrt(b**2 / (a**2 + b**2))
    x = a * y / b
    print(f"{x:.10} {y:.10}")
elif a == 0:
    y = 1.0
    x = 0.0
    print(f"{x:.10} {y:.10}")
else:
    y = 0.0
    x = 1.0
    print(f"{x:.10} {y:.10}")
