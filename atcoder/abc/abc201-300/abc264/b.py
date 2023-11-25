r, c = map(int, input().split())

if min(min(r, (16 - r)), min(c, (16 - c))) % 2 == 1:
    print("black")
else:
    print("white")