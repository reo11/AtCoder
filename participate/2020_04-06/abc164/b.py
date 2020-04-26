a, b, c, d = map(int, input().split())

i = 0
while True:
    if a <= 0:
        print("No")
        exit()
    elif c <= 0:
        print("Yes")
        exit()
    if i % 2 == 0:
        c -= b
    else:
        a -= d
    i += 1
