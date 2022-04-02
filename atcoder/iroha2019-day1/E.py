n, a, b = map(int, input().split())
if b > 0:
    d = list(map(int, input().split()))
    d.sort()
    date = 0
    l = 1

    for value in d:
        date += (value - l) // a
        date += 1
        l = value + 1
    date += (n + 1 - l) // a
    print(n - date)
else:
    print(n - (n // a))
