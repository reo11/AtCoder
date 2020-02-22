n, k = map(int, input().split())

i = 0
while True:
    s = k ** i
    if n / s >= 1:
        i += 1
        continue
    else:
        break
print(i)