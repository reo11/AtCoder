n, a, b = map(int, input().split())
if b > 0:
    d = list(map(int, input().split()))
    d.sort()
    date = 0
    left = 1

    for value in d:
        date += (value - left) // a
        date += 1
        left = value + 1
    date += (n + 1 - left) // a
    print(n - date)
else:
    print(n - (n // a))
