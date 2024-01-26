b = int(input())

for i in range(1, 10**6 + 1):
    if i**i > b:
        break
    if i**i == b:
        print(i)
        exit()
print(-1)
