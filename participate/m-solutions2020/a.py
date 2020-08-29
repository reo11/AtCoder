x = int(input())

for i, j in zip(range(4, 19, 2), range(8, 0, -1)):
    if i * 100 <= x <= (i + 2) * 100 - 1:
        print(j)
        exit()