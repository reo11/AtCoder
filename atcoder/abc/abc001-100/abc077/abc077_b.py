n = int(input())

idx = 0
while True:
    idx += 1
    if idx**2 > n:
        idx -= 1
        break

print(idx**2)
