y = int(input())

for i in range(y, 4000):
    if i % 4 == 2:
        print(i)
        exit()