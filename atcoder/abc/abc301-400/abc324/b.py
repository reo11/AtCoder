n = int(input())

for x in range(70):
    for y in range(40):
        if 3**y > n:
            break
        if 2**x * 3**y == n:
            print("Yes")
            exit()
    if 2**x > n:
        break
print("No")
