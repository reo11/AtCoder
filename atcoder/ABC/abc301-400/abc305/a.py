n = int(input())

if n % 5 <= 2:
    print(n - n % 5)
else:
    print(n + 5 - (n % 5))
