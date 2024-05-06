n, x, y, z = map(int, input().split())

from_x = min(x, y)
until_x = max(x, y)

for i in range(from_x, until_x+1):
    if i == z:
        print("Yes")
        exit()

print("No")
