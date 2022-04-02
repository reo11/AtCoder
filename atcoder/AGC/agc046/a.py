x = int(input())
for n in range(3, 361):
    if n * x % 360 == 0:
        print(n)
        exit()
