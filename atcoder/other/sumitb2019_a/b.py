from math import floor
n = int(input())

for x in range(n+1):
    cost = floor(x * 1.08)
    if cost == n:
        print(x)
        exit()
print(":(")