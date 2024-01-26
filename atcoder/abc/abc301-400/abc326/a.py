x, y = map(int, input().split())
a = x - y
if (a > 0 and a <= 3) or (a < 0 and a >= -2):
    print("Yes")
else:
    print("No")
