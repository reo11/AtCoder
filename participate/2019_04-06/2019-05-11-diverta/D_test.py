for n in range(1, 101):
    for i in range(1, n):
        if n % i == n//i:
            print(n, i, n%i)