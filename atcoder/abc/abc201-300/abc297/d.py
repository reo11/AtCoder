import math

a, b = map(int, input().split())

count = 0
while True:
    diff = abs(a - b)
    if a == b:
        break
    elif a < b:
        if a != 0:
            c = max(1, (diff // a))
        else:
            c = 1
        b = b - (c * a)
        count += c
    else:
        if b != 0:
            c = max(1, (diff // b))
        else:
            c = 1
        a = a - (c * b)
        count += c
print(count)
