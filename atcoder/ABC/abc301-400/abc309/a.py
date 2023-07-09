a, b = map(int, input().split())

if b - a == 1 and a not in [3, 6]:
    print("Yes")
else:
    print("No")