m = int(input())
d = list(map(int, input().split()))

list = []

for month in range(1, m + 1):
    for day in range(1, d[month - 1] + 1):
        list.append([month, day])

print(f"{list[len(list) // 2][0]} {list[len(list) // 2][1]}")