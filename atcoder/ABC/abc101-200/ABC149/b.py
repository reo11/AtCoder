a, b, k = map(int, input().split())
b_ = b
if a - k < 0:
    b_ = b + (a - k)
print(max(0, a - k), max(0, b_))