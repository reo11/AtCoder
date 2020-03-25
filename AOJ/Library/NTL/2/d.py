a, b = map(int, input().split())
if a < 0 and b >= 0 or a >= 0 and b < 0:
    print(0 - abs(a) // abs(b))
else:
    print(a//b)