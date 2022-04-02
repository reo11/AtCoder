n = int(input())

c = 0
for i in range(1, n + 1):
    if i % 2 == 1:
        c += 1
s = c / n

print(s)
